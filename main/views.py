
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response, redirect
import random
import django.contrib.auth as auth
from django.views import View

from main import models
from main import forms


def base_view(request):
    # questions_list = []
    questions_list = models.Question.objects.all()
    # for question in questions_list:
    #         question.text = question.text[:120] + "..."
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
                                             "top_users": ["your ", "your2", "your3"],
                                                      })


def hot_questions(request):
    # questions_list = []
    questions_list = models.Question.objects.all()
    # for question in questions_list:
    #         question.text = question.text[:120] + "..."
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

    return render(request, 'hot_questions.html', {
        "user_photo": "user_avatars/User_Avatar.png",
        "questions": questions,
        "pop_tags": ["pop_tag1", "pop_tag2", "pop_tag3"],
        "top_users": ["your ", "your2", "your3"],
    })


def new_question_view(request):
    return render(request, 'new_question.html', {})


class QuestionView(View):
    def get(self, request, id):
        question = models.Question.objects.get(pk=id)

        answers_list = models.Answer.objects.filter(quest=id)
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

        return render(request, 'question.html', {"question": question,
                                                 "answers": answers,
                                                 })


# def question_view(request, question_id):
#     question = models.Question.objects.get(pk=question_id)
#     answers_list = models.Answer.objects.all().filter(question=question_id)
#
    # answers_list = []
    # question = {"tags": ["tag1", "tag2", "tag3"],
    #             "title": "Question_Title",
    #             "text":  "bar " * 300 + "...",
    #             'rating': 10,
    #             }
    # for i in range(100):
    #     answers_list.append({"title": "Title" + str(i + 1), "text": "bla " * 30 + "...",
    #                         "rating": random.randint(0, 100)})

    # paginator = Paginator(answers_list, 3)
    # page = request.GET.get('page')
    #
    # try:
    #     answers = paginator.page(page)
    # except PageNotAnInteger:
    #     If page is not an integer, deliver first page.
        # answers = paginator.page(1)
    # except EmptyPage:
    #     If page is out of range (e.g. 9999), deliver last page of results.
        # answers = paginator.page(paginator.num_pages)
    #
    # return render_to_response('question.html', {"question": question,
    #                                             "answers": answers,
    #                                             })


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

    return render(request, 'tag_questions.html', {"questions": questions,
                                             "pop_tags": ["pop_tag1", "pop_tag2", "pop_tag3"],
                                             "top_users": ["User", "Pasha", "Masha"],
                                             })


def settings_view(request):
    return render(request, 'settings.html')


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


def logout_view(request):
    auth.logout(request)
    return redirect('/')
