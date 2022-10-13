from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
	t = question["text"]
	a = question["answer"]
	question_bank.append(Question(t, a))

quiz = QuizBrain(question_bank)

while quiz.still_remaining_questions():
	quiz.next_question()

print("You've completed the all the questions")
print(f"Your final score is {quiz.score}/{quiz.question_number}")