"""Turtle module."""
from turtle import Turtle

from time import sleep


def main():
    """My function."""
    turtle = Turtle()
    turtle.showturtle()  # графическое окно с черепашкой
    sleep(5)
    turtle.forward(100)  # переместить черепашку вперед на 100 пикселей
    sleep(5)
    turtle.backward(250)  # переместить черепашку назад на 250 пикселей
    sleep(5)
    turtle.right(90)  # поворачивает черепашку вправо на 90 градусов
    sleep(5)
    turtle.left(120)  # поворачивает черепашку влево на 120 градусов
    sleep(5)


if __name__ == "__main__":
    main()
