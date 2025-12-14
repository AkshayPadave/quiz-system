from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Quiz

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    all_questions = quiz.question_set.all()
    print(f"***** {all_questions}")
    return render(request, 'quiz/take_quiz.html', {"quiz": quiz, "questions": all_questions})


def submit_quiz(request, quiz_id):
    return f"You have submitted quiz {quiz_id}"