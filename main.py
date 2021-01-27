from playsnake import PlaySnake
from turtle import Screen
start_screen = Screen()
user_bet = start_screen.textinput(title="Start the Game",prompt='')
play = PlaySnake()
play.play_start()
