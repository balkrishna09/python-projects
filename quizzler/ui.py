from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quizz_brain: QuizBrain):
        self.quiz= quizz_brain
        self.window = Tk()
        self.window.title('quizz')
        self.window.config(padx=30, pady=50, bg=THEME_COLOR)

        # right button
        right_img = PhotoImage(file='images/true.png')
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=1, row=3)

        # false button
        wrong_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=wrong_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=2, row=3)
        # self.canvas.create_image(100, 97, image=img)
        # self.canvas.grid(column=1,row=1)

        # score label
        self.score_label = Label(text="Score : 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=2, row=1)

        # canvas for question
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280,text='question here', fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text=f'End of the quiz game your final score is {self.quiz.score}')
            self.right_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(700, self.get_next_question)


