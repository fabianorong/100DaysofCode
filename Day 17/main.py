from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
    if quiz.still_has_questions() == False:
        finalscore, finalquestionnumber = quiz.scores()
        print("You completed the quiz")
        print(f"Your final score was: {finalscore}/{finalquestionnumber}")