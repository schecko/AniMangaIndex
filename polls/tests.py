from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Question

class QuestionModelTests(TestCase):
    def testWasPublishedInFuture(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futureQuestion = Question(pub_date=time)
        self.assertIs(futureQuestion.was_published_recently(), 
        False)

