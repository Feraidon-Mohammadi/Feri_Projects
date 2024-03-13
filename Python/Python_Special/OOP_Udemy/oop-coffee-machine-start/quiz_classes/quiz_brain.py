from question_model import Question
from typing import List
class QuizBrain:
    def __init__(self, q_list: List[Question])-> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self)-> bool:
        return self.question_number < len(self.question_list)

    def next_question(self)->None:

        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text}.(True/False)").lower()
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer:bool, correct_answer: bool)->None:
        if user_answer == correct_answer.lower() :
            print("Congratulations :) correct Answer! ")
            self.score += 1
            print(f"Score: {self.score} of {self.question_number+1}")
            print(f"correct answer is: {correct_answer}")
            print("-" * 120)

        else:
            print("Sorry your input answer is not correct, True or False nothing ")
            print(f"Score: {self.score} of {self.question_number + 1}")
            print(f"correct answer is: {correct_answer}")
            print("-" * 120)


