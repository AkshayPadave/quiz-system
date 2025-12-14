from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Quiz, QuizResult, Question, Choice

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    all_questions = quiz.question_set.all()
    print(f"***** {all_questions}")
    return render(request, 'quiz/take_quiz.html', {"quiz": quiz, "questions": all_questions})


def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()

    total = 0

    for q in questions:
        user_answer = request.POST.get(str(q.id))
        if q.question_type == 'mcq' or q.question_type == 'tf':
            correct_choice = q.choices.filter(is_correct=True).first()
            if correct_choice and user_answer == correct_choice.text:
                total += 1
        elif q.question_type == 'text':
            if user_answer and user_answer.strip().lower() == "correct answer":
                total += 1
    
    QuizResult.objects.create(quiz=quiz, score=total)
    return render(request, 'quiz/quiz_result.html', {"quiz": quiz, "score": total})
