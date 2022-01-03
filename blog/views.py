from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
import stripe
from .forms import MemberProfileForm, UserRegisterForm, MemberProfileUpdateForm
from django.conf import settings
from django.contrib import messages
from .models import Package, OrderDetail, Member
from question.models import MemberCompletedTopic, MemberSolvedQuestion, Topic, Question
from django.views.generic import DetailView, TemplateView
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta, date
import requests
from django.contrib.auth.decorators import login_required
from question.views import member_subjects
from question.models import Topic
from question.decorators import allowed_users
from django.contrib.auth.models import Group


def home(request):
    return render(request, 'blog/home.html')


def feexam(request):
    return render(request, 'blog/feexam.html')


def quest(request):
    context = {
        'Question': Question
    }
    return render(request, 'blog/question.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, "Congratulations !!! New Account created successfully :)")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/profile/")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Stripe payment views

@login_required
def package_detail_view(request, id):
    context = {}
    try:
        context['member'] = Member.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse('profile'))

    context['object'] = Package.objects.get(id=id)
    context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY

    return render(request, 'blog/payment/product_detail.html', context)



@csrf_exempt
def create_checkout_session(request, id):
    request_data = json.loads(request.body)
    product = get_object_or_404(Package, pk=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        customer_email=request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price*100)
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    member = Member.objects.get(user=request.user)

    order = OrderDetail()
    order.customer_email = member.email
    order.product = product
    order.user = request.user
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price*100)
    order.save()

    return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = "blog/payment/success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(
            OrderDetail, stripe_payment_intent=session.payment_intent)
        order.has_paid = True
        order.save()

        member = Member.objects.get(user=request.user)
        member.order_details = order
        member.purchase_time = datetime.now()
        validity = 28 * order.product.validity_in_months
        member.package_expiration_time = datetime.now() + timedelta(days=validity)
        member.save()

        member_group = Group.objects.get(name="member")
        member_group.user_set.add(request.user)

        return render(request, self.template_name)


class PaymentFailedView(TemplateView):
    template_name = 'blog/payment/payment_failed.html'


def profile(request):
    if request.method == "POST":
        form = MemberProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            country = form.cleaned_data['country']
            discipline = form.cleaned_data['discipline']
            appearing_year = form.cleaned_data['appearing_year']
            usr.email = email
            usr.save()

            try:
                reg = Member.objects.get(user=usr)
                reg.first_name = first_name
                reg.last_name = last_name
                reg.email = email
                reg.country = country
                reg.appearing_year = appearing_year
                reg.save()
            except:
                reg = Member(user=usr, first_name=first_name, last_name=last_name, email=email,
                             country=country, discipline=discipline, appearing_year=appearing_year)
                reg.save()
            messages.success(
                request, 'Congratulations!! Profile updated Successfully!!!')
            return HttpResponseRedirect(reverse('blog-home'))
    else:
        if Member.objects.filter(user=request.user).exists():
            form = MemberProfileUpdateForm()
            action = "Update Profile"
            note = None
        else:
            form = MemberProfileForm()
            action = "Create New Profile"
            note = "Display note"
        return render(request, 'users/profile.html', {'form': form, 'action': action, 'note': note})


def get_quote():
    try:
        response = requests.get('https://api.quotable.io/random')
        if response.status_code != 404:
            json_data = response.json()
            quote = json_data['content']
            author = json_data['author']
            quote_data = {
                'quote': quote,
                'author': author,
            }
            return quote_data
        else:
            quote_data = {
                'quote': "error while getting quote",
            }
    except:
        print("Something went wrong while fetching quotes")


@login_required
@allowed_users(allowed_roles=['member'])
def dashboard(request):
    member = Member.objects.get(user=request.user)
    date_now = date.today()
    if member.package_expiration_time.date() < date_now:
        member_group = Group.objects.get(name="member")
        member_group.user_set.remove(request.user)
    quote_data = get_quote()
    question_solved = MemberSolvedQuestion.objects.filter(
        member=member).order_by('id')[:5][::-1]
    no_of_questions_solved = MemberSolvedQuestion.objects.filter(
        member=member).count
    topic_completed = MemberCompletedTopic.objects.filter(member=member)
    topics = Topic.objects.all().count()
    subjects = member_subjects(request.user)
    context = {
        'quote_data': quote_data,
        'member': member,
        'question_solved': question_solved,
        'topic_completed': topic_completed,
        'topics': topics,
        'subjects': subjects,
        'no_of_question_solved': no_of_questions_solved,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def redirect(request):
    try:
        member = Member.objects.get(user=request.user)
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/profile/')
