import turtle
from T import *
lag(2)
clear_screen()
try:
    emma = turtle.Turtle()
    for i in range(5):
        emma.fd(150)
        emma.right(144)
    turtle.bye()
    lag(1)
    p("Passed.")
    lag(1)
except:
    p("You can't see the star... but you can still play")
