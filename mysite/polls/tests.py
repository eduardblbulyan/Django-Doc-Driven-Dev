from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=90)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# $ python3 manage.py test polls
