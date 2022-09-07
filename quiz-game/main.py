from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)

quiz=QuizzBrain(question_bank)

while quiz.remaining_questions():
    quiz.next_question()
print(f'you completed the quiz and you final score was : {quiz.score}/{quiz.question_number}')