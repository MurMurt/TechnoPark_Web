from django.urls import path, include

from main.views import base_view, new_question_view, \
    tag_questions_view, settings_view, hot_questions, login, logout_view, QuestionView

app_name = 'main'
urlpatterns = [
    path(r'', base_view),
    path(r'hot', hot_questions),
    path(r'new_question/', new_question_view),
    path(r'question/<int:id>/', QuestionView.as_view(), name='question'),
    path(r'tag', tag_questions_view),
    path(r'settings', settings_view),
    path(r'signin', login),
    path(r'logout/', logout_view),

]
