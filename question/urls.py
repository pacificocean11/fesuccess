from django.urls import path
from .import views

app_name = "content"

urlpatterns = [
    # Questions models urls
    path('check-answer/', views.check_answer, name="check-answer"),

    path('search/', views.search, name="search"),

    path('<subject>/', views.subject, name="subject"),

    path('<subject>/<topic>/', views.subject, name="subject"),

    path('theory/<subject>/<topic>/<subtopic>/', views.theory, name="theory"),

    path('solved-examples/<subject>/<topic>/<subtopic>/',
         views.solved_example_list, name="solved-example"),

    path('question/<subtopic>/<question_slug>/',
         views.question, name="question"),

]
