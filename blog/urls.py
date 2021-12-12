from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('feexam/', views.feexam, name='blog-feexam'),
    path('quest/', views.quest, name='blog-quest'),

    # Stripe payment urls

    path('details/<id>/', views.PackageDetailView.as_view(), name='details'),

    path('api/checkout-session/<id>/',
         views.create_checkout_session, name='api_checkout_session'),

    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    path('failed/', views.PaymentFailedView.as_view(), name='failed'),

    # User Authentication
    path('register/', views.register, name='register'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="users/login.html",
                                                         authentication_form=LoginForm), name="login"),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
]
