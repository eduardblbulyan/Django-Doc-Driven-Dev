from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        ("Content", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]

admin.site.register(Question, QuestionAdmin)
