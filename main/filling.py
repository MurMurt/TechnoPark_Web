import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")
django.setup()

import random
from main.models import Question, Answer, Tag
from ask.settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from faker import Faker

from django.contrib.auth import get_user_model
User = get_user_model()

fake = Faker()


def create_users(n):
    for _ in range(n):
        u = User.objects.create_user(username=fake.user_name(),
                                                email=fake.email(),
                                                password="311097gii"
                                                )
        u.save()


def create_tags(n):
    for _ in range(n):
        t = Tag(title=fake.word())
        t.save()


def create_questions(n):
    profile_id_list = [user for user in User.objects.all()]
    tags_list = [tag.pk for tag in Tag.objects.all()]
    for _ in range(n):
        u_id = random.choice(profile_id_list)
        q = Question(author=u_id,
                     title=fake.sentence(),
                     text=fake.text()
                     )
        q.save()
        for _ in range(random.randint(1, 3)):
            t_id = random.choice(tags_list)
            q.tags.add(t_id)

        q.save()

        create_answers(random.randint(1, 10), q)
        for i in range(10):
            create_like(q)


def create_answers(n, question):
    profile_id_list = [user for user in User.objects.all()]
    for _ in range(n):
        u_id = random.choice(profile_id_list)
        a = Answer(author=u_id,
                   quest=question,
                   text=fake.text()
                   )
        a.save()


def create_like(question_id):
    profile_id_list = [user for user in User.objects.all()]
    q = Question.objects.get(pk=question_id)
    q.like(random.choice(profile_id_list))
    q.save()



# create_users(3)
# create_tags(20)
create_questions(3)