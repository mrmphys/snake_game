from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


class PlaySnake:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My snake game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.score = ScoreBoard()

        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.game_is_on = True

    def play_start(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.15)
            self.snake.move()

            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.extend()
                self.score.add_score()

            if self.snake.head.xcor() > 285 or self.snake.head.xcor() < -285 or self.snake.head.ycor() > 285 \
                    or self.snake.head.ycor() < -285:
                self.game_is_on = False
                self.score.game_over()

            for segment in self.snake.segment_list[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.score.game_over()

        self.screen.exitonclick()
