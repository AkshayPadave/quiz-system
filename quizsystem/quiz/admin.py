from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, Choice, QuizResult

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)