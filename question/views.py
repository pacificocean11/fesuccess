from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.template.loader import render_to_string


def member_subjects(user):
    member = Member.objects.get(user=user)
    member_discipline = member.discipline
    member_subjects = Subject.objects.filter(
        related_disciplines=member_discipline)
    return member_subjects


@login_required
@allowed_users(allowed_roles=['member'])
def subject(request, subject, topic=""):
    sub = Subject.objects.get(slug=subject)
    topics = Topic.objects.filter(related_subjects=sub)
    member = Member.objects.get(user=request.user)

    if topic == "":
        display_topic = topics[0]
    else:
        display_topic = Topic.objects.get(slug=topic)

        if not MemberCompletedTopic.objects.filter(topic=display_topic, member=member).exists():
            MemberCompletedTopic.objects.create(
                topic=display_topic, member=member)

    display_subtopic = SubTopic.objects.filter(
        Q(topic=display_topic) & Q(related_subject=sub))

    context = {
        'topics': topics,
        'member': member,
        'subject': sub,
        'subtopic': display_subtopic,
        'current_topic': display_topic,
    }
    return render(request, 'dashboard/topic.html', context)


@login_required
@allowed_users(allowed_roles=['member'])
def theory(request, subject, topic, subtopic=""):
    member = Member.objects.get(user=request.user)
    subject = Subject.objects.get(slug=subject)
    topic = Topic.objects.get(slug=topic)
    current_subtopic = SubTopic.objects.get(slug=subtopic)
    subtopics = SubTopic.objects.filter(
        Q(topic=topic) & Q(related_subject=subject))
    context = {
        'subject': subject,
        'topic': topic,
        'current_subtopic': current_subtopic,
        'subtopics': subtopics,
        'member': member,
    }
    return render(request, 'dashboard/theory.html', context)


@login_required
@allowed_users(allowed_roles=['member'])
def solved_example_list(request, subject, topic, subtopic):
    member = Member.objects.get(user=request.user)
    subject = Subject.objects.get(slug=subject)
    topic = Topic.objects.get(slug=topic)
    current_subtopic = SubTopic.objects.get(slug=subtopic)
    subtopics = SubTopic.objects.filter(
        Q(topic=topic) & Q(related_subject=subject))
    questions = Question.objects.filter(Q(subtopic=current_subtopic))
    context = {
        'subject': subject,
        'topic': topic,
        'current_subtopic': current_subtopic,
        'subtopics': subtopics,
        'member': member,
        'questions': questions,
    }
    return render(request, 'dashboard/solved_example_list.html', context)


@login_required
@allowed_users(allowed_roles=['member'])
def question(request, subtopic, question_slug):
    member = Member.objects.get(user=request.user)
    current_question = Question.objects.get(slug=question_slug)
    subtopic = SubTopic.objects.get(slug=subtopic)
    questions = Question.objects.filter(Q(subtopic=subtopic))
    tag_text = current_question.comma_saperated_tags
    question_tags = tag_text.split(',')
    try:
        solved_question = MemberSolvedQuestion.objects.get(
            Q(member=member) & Q(question=current_question))
    except:
        solved_question = None

    context = {
        'member': member,
        'current_question': current_question,
        'subtopic': subtopic,
        'questions': questions,
        'question_tags': question_tags,
        'solved_question': solved_question,
    }
    return render(request, 'dashboard/question.html', context)


def check_answer(request):
    if request.method == "POST":
        selected_answer = request.POST['selected_answer']
        question_slug = request.POST['question_slug']
        member = Member.objects.get(user=request.user)

        question = Question.objects.get(slug=question_slug)
        try:
            solved_question = MemberSolvedQuestion.objects.get(
                member=member, question=question)
        except:
            MemberSolvedQuestion.objects.create(
                member=member, question=question)
        solution_image = question.solution_image
        solution = question.solution
        correct_answer = question.correct_choice
        if int(selected_answer) == correct_answer:
            correct = 1
        else:
            correct = 0

        response = {
            "correct": correct,
            "correct_option": correct_answer,
            "solution": solution,
            "solution_image": solution_image,
        }

        return JsonResponse(response)


def search(request):
    url_parameter = request.GET.get('q')
    if url_parameter:
        searched_topics = Topic.objects.filter(
            topic_name__icontains=url_parameter)
    else:
        searched_topics = Topic.objects.all()

    print(searched_topics)
    ctx = {}

    ctx['topics'] = searched_topics

    if request.is_ajax():
        html = render_to_string(
            template_name="dashboard/topics-results-partial.html",
            context={"searched_topics": searched_topics}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "dashboard/dashboard.html", context=ctx)
