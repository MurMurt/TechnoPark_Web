from django.urls import path, include

from main.views import base_view, new_question_view, question_view, \
    tag_questions_view, settings_view, signin_view

urlpatterns = [
    path(r'', base_view),
    path(r'new_question/', new_question_view),
    path(r'question/', question_view),
    path(r'tag', tag_questions_view),
    path(r'settings', settings_view),
    path(r'signin', signin_view)

]
