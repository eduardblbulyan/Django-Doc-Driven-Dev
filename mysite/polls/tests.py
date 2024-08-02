from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=90)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_questinon = Question(pub_date=time)
        self.assertIs(recent_questinon.was_published_recently(), True)



# $ python3 manage.py test polls

# --> To test a view <--

"""
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
# create an instance of the client for our use
>>> client = Client()
>>> response = client.get("/") # or /polls
>>> response.status_code

>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
>>> response.content
>>> response.context["latest_question_list"]
"""