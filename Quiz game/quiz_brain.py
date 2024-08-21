class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def next_question(self):
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            if input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ") == current_question.answer:
                print("You got it right")
                self.score += 1
                print(f"Your current score is {self.score}/{self.question_number+1}")
            else:
                print("That was wrong answer")
                print(f"Your current score is {self.score}/{self.question_number+1}")
            self.question_number += 1
    def find_result(self):
        print(f"\n\n\nYour final Score is {self.score}")
