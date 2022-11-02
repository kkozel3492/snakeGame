import turtle
from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=0, y=245)
        self.score = 0
        self.color("White")
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(x=0, y=0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)

class GameDetails(Turtle):

    def __init__(self):
        super().__init__()

    def playAgain(self,Scoreboard):
        score = Scoreboard.score
        playAgain = turtle.textinput(f"Your final score is {score}", "Do you want to play again? 'y' or 'n'").lower()
        return playAgain






