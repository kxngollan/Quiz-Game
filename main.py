from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for question in question_data:
    questions.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()