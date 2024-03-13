from question_model import  Question
from quiz_brain import  QuizBrain
from data import question_data






question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()






