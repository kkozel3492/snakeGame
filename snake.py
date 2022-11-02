from turtle import Turtle

STARTING_POSTITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

#Create the snake
    def createSnake(self):
        for i in STARTING_POSTITIONS:
            self.addSegment(i)

    def __init__(self):
        self.body = []
        self.createSnake()
        self.head = self.body[0]

    def addSegment(self, position):
        bodySegment = Turtle("square")
        bodySegment.color("White")
        bodySegment.penup()
        bodySegment.goto(position)
        self.body.append(bodySegment)

    def extend(self):
        self.addSegment(self.body[-1].position())


    #Move the snake
    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            newX = self.body[seg - 1].xcor()
            newY = self.body[seg - 1].ycor()
            self.body[seg].goto(newX, newY)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
