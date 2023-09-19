"""Snake game code in Python
This code implements a simple snake game using the Turtle library.
The player controls the snake using the arrow keys,
and the goal is to eat as many food items as possible without hitting the wall or itself."""
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')


game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(0.1)

    snake.move()
    # game_is_on = snake.check()
    # score.over(game_is_on)
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > +290 or snake.head.ycor() < -290:
        game_is_on = False
        score.over()
    elif snake.detect_hit() == False:
        game_is_on = False
        score.over()

    if snake.head.distance(food) < 18:
        food.reset_pos()
        score.reset_score()
        snake.rise_snake()

screen.exitonclick()