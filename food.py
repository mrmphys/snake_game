from turtle import Turtle
import random

FOOD_DEFAULT_POSITION = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        food_x = random.randint(-FOOD_DEFAULT_POSITION, FOOD_DEFAULT_POSITION)
        food_y = random.randint(-FOOD_DEFAULT_POSITION, FOOD_DEFAULT_POSITION)
        self.goto(food_x, food_y)

    def refresh(self):
        food_x = random.randint(-FOOD_DEFAULT_POSITION, FOOD_DEFAULT_POSITION)
        food_y = random.randint(-FOOD_DEFAULT_POSITION, FOOD_DEFAULT_POSITION)
        self.goto(food_x, food_y)
