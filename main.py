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

# Creating the car manager
car = CarManager()
car.hideturtle()

# Creating the scoreboard
scoreboard = Scoreboard()

# Listen to keystroke
screen.listen()
screen.onkey(player.up, 'w')
screen.onkey(player.up, 'Up')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # Detect collision with car
    for c in car.all_cars:
        if c.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()


screen.exitonclick()
