from turtle import Turtle


class Dashboard(Turtle):

    def __init__(self):
        super().__init__()
        self.id = 1
        self.write(f"User id: {self.id}", align="center", font=("Arial", 8, "normal"))