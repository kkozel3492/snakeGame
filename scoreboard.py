import turtle
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.goto(x=0, y=245)
        self.color("White")
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High-score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highScore}')

        self.score = 0
        self.updateScoreboard()


class GameDetails(Turtle):

    def __init__(self):
        super().__init__()

    def playAgain(self, Scoreboard):
        score = Scoreboard.score
        playAgain = turtle.textinput(f"Your final score is {score}", "Do you want to play again? 'y' or 'n'").lower()
        return playAgain




