from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
  text = question_data[i]["text"]
  answer = question_data[i]["answer"]

  question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")