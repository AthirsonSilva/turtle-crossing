import time

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from turtle import Screen

# Creating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating the player
player = Player()

# Listen to keystroke
screen.listen()
screen.onkey(player.up, 'w')
screen.onkey(player.up, 'Up')


game_is_on = True
loops = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loops += 1
    if loops % 6 == 0:
        pass

    print(loops)

screen.exitonclick()
