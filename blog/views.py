from django.shortcuts import render
from django.http import HttpResponse


Question = [
    {
        'Qnum': "XYZ-01",
        'Qtext': "My name is Slim Shady"
    }
]


def home(request):
    return render(request, 'blog/home.html')


def feexam(request):
    return render(request, 'blog/feexam.html')


def quest(request):
    context = {
        'Question': Question
    }
    return render(request, 'blog/question.html', context)
