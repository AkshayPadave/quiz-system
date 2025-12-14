from django.db import models

"""
Create your models here.
Build a Quiz Management System with:
Admin Panel
Ability to create a quiz with:
Quiz title
A few questions of various types (MCQ, True/False, text, etc.)
"""



QUESTION_TYPES = [
        ('MCQ', 'Multiple Choice Question'),
        ('TF', 'True/False'),
        ('TEXT', 'Text Answer'),
    ]

# Creating Quiz model
class Quiz(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    


# Creating Question model
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=4, choices=QUESTION_TYPES)

    def __str__(self):
        return self.text
    

# Creating Choice model for MCQ type questions
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


# Creating Answer model to store answers
class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quiz.title} - {self.score}"
