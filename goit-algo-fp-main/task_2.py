import turtle
import math


def draw_pythagoras_tree(t, order, size):
    if order == 0:
        t.forward(size)
        t.backward(size)
    else:
        t.forward(size)
        t.left(45)
        draw_pythagoras_tree(t, order - 1, size / math.sqrt(2))
        t.right(90)
        draw_pythagoras_tree(t, order - 1, size / math.sqrt(2))
        t.left(45)
        t.backward(size)


def draw_tree(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -size * 3)
    t.pendown()
    t.left(90)

    draw_pythagoras_tree(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    try:
        recursion_level = int(
            input("Введіть рівень рекурсії (наприклад, 5): "))
        if recursion_level < 0:
            print("Рівень рекурсії має бути невід'ємним числом!")
        else:
            draw_tree(recursion_level)
    except ValueError:
        print("Будь ласка, введіть ціле число.")
