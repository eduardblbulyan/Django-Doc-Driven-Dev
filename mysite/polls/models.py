from django.db import models
from django.utils import timezone
from datetime import timedelta

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text   
    
    def was_published_recently(self):
        now = timezone.now()
        return now-timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Some lookups

# Question.objects.filter(id=1)
# Question.objects.filter(question_text__startswith="What")


# Get question that published this year
# from django.utils import timezone
# current_year = timezone.now().year
# Question.objects.get(pub_date__year=current_year)

# Lookup by primary key
# Question.objects.get(pub_date__year=current_year)


# --Giving Question couple of Choices
# q = Question.objects.get(pk=1)
# q.choice_set.all() --> <QuerySet []>
# q.choice_set.create(choice_text="Not much", votes=0)
# q.choice_set.create(choice_text="The sky", votes=0)
# c = q.choice_set.create(choice_text="Just hacking again", votes=0)
# c.question
# q.choice_set.all()
# Choice.objects.filter(question__pub_date__year=current_year)
# c = q.choice_set.filter(choice_text__startswith="Just")
# c.delete()