import sys
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard, GameDetails

def snakeGame():
#Set up screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    # Create a snake body
    gameSnake = Snake()
    food = Food()
    scoreboard = Scoreboard()

#Start the game

    gameIsOn = True
    while gameIsOn:
        screen.update()
        time.sleep(0.1)
        gameSnake.move()
        screen.listen()
        screen.onkey(gameSnake.up, "Up")
        screen.onkey(gameSnake.left, "Left")
        screen.onkey(gameSnake.down, "Down")
        screen.onkey(gameSnake.right, "Right")


        # Detect collision with food
        if gameSnake.head.distance(food) < 15:
            food.refresh()
            gameSnake.extend()
            scoreboard.increaseScore()


        # Detect collision with wall
        if gameSnake.head.xcor() > 280 or gameSnake.head.xcor() < -280 or gameSnake.head.ycor() > 280 or gameSnake.head.ycor()  < -280:
            scoreboard.reset()
            gameSnake.reset()
            # gameIsOn = False

        #Detect collision with snake
        for segment in gameSnake.body[1:]:
            if gameSnake.head.distance(segment) < 10:
                gameSnake.reset()
                scoreboard.reset()

    newScrn = GameDetails()
    keepPlaying = newScrn.playAgain(scoreboard)
    if keepPlaying == 'y':
        gameIsOn = True
        screen.clear()
        snakeGame()
    else:
        sys.exit()

    screen.exitonclick()

snakeGame()

