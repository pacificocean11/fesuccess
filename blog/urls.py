from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MySetPasswordForm

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
    path('redirect/', views.redirect, name="redirect"),

    path('register/', views.register, name='register'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="users/login.html",
                                                         authentication_form=LoginForm), name="login"),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),

    path('profile/', views.profile, name="profile"),

    path('dashboard/', views.dashboard, name="dashboard"),

    # password reset
    path('password-reset/', auth_views.PasswordResetView.as_view
         (template_name='pwdrst/password_reset.html', form_class=MyPasswordResetForm), name="password-reset"),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view
         (template_name='pwdrst/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
         (template_name='pwdrst/password_reset_confirm.html',
          form_class=MySetPasswordForm), name="password_reset_confirm"),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view
         (template_name='pwdrst/password_reset_complete.html'), name="password_reset_complete"),


]
