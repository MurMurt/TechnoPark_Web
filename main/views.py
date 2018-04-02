import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import random
# Create your views here.
from django.template import loader, RequestContext


def base_view(request):
    questions_list = []
    for i in range(100):
        questions_list.append({"title": "Title" + str(i + 1), "text": "bla " * 30 + "...",
                               "tags": ["tag1", "tag2", "tag3"],
                               "rating": random.randint(0, 100), "answers": random.randint(3, 100)})

    paginator = Paginator(questions_list, 5)
    page = request.GET.get('page')

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {"questions": questions,
                                             "pop_tags": ["pop_tag1", "pop_tag2", "pop_tag3"],
                                             "top_users": ["your mom", "your mommy", "your mamka"],
                                             })


def new_question_view(request):
    return render_to_response('new_question.html', {})


def question_view(request):
    answers_list = []
    question = {"tags": ["tag1", "tag2", "tag3"],
                "title": "Question_Title",
                "text":  "bar " * 300 + "...",
                'rating': 10,
                }
    for i in range(100):
        answers_list.append({"title": "Title" + str(i + 1), "text": "bla " * 30 + "...",
                            "rating": random.randint(0, 100)})

    paginator = Paginator(answers_list, 3)
    page = request.GET.get('page')

    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        answers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        answers = paginator.page(paginator.num_pages)

    return render_to_response('question.html', {"question": question,
                                                "answers": answers,
                                                })


def tag_questions_view(request):
    questions_list = []
    for i in range(100):
        questions_list.append({"title": "Title" + str(i + 1), "text": "bla " * 30 + "...",
                               "tags": ["tag1", "tag2", "tag3"],
                               "rating": random.randint(0, 100), "answers": random.randint(3, 100)})

    paginator = Paginator(questions_list, 5)
    page = request.GET.get('page')

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    return render_to_response('tag_questions.html', {"questions": questions,
                                             "pop_tags": ["pop_tag1", "pop_tag2", "pop_tag3"],
                                             "top_users": ["your mom", "your mommy", "your mamka"],
                                             })


def settings_view(request):
    return render_to_response('settings.html', {'user': {'username': 'IVAN'}})


def signin_view(request):
    return render_to_response('signin.html', {})
