from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # creates a food object at a random location on the screen
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        self.refresh()

    def refresh(self):
        # this method creates a new food piece, activates when the snake object collides with the food object
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
