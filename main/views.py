import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
import random
import django.contrib.auth as auth
from django.views.generic import FormView

from main import forms
from main.models import User
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

    return render(request, 'index.html', {
                                             "user_photo": "user_avatars/User_Avatar.png",
                                            "questions": questions,
                                             "pop_tags": ["pop_tag1", "pop_tag2", "pop_tag3"],
                                             "top_users": ["your mom", "your mommy", "your mamka"],
                                                      })

def hot_questions(request):
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

    return render_to_response('hot_questions.html', {"questions": questions,
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
                                             "top_users": ["User", "Pasha", "Masha"],
                                             })


def settings_view(request):
    return render_to_response('settings.html', {'user': {'username': 'IVAN'}})


def login(request):
    args = {}
    args['form'] = forms.Login()
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользовватель не найден'
            return render(request, 'signin.html', args)
    else:
        return render(request, 'signin.html', args)


class LogIn(FormView):
    template_name = 'signin.html'
    form_class = forms.Login
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('/')
