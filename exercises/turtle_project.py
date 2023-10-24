"""Drawing of Kirby using Turtle."""
__author__ = "930690385"
from turtle import Turtle, colormode, done
from random import randint

colormode(255)
star: Turtle = Turtle()
kirby: Turtle = Turtle()
right_leg: Turtle = Turtle()
left_leg: Turtle = Turtle()
right_blush: Turtle = Turtle()
left_blush: Turtle = Turtle()
right_eye: Turtle = Turtle()
left_eye: Turtle = Turtle()
right_shine: Turtle = Turtle()
left_shine: Turtle = Turtle()


# colors for kirby
body_color: tuple[int, int, int] = (250, 160, 160)
mouth_color: tuple[int, int, int] = (165, 42, 42)
leg_color: tuple[int, int, int] = (227, 11, 92)
blush_color: tuple[int, int, int] = (255, 69, 122)
eye_color: tuple[int, int, int] = (0, 0, 0)
shine_color: tuple[int, int, int] = (255, 255, 255)
tongue_color: tuple[int, int, int] = (248, 20, 72)


# sizes for the ovals
leg_size: list[float] = [10.0, 5.0, 2.0]
blush_size: list[float] = [2.5, 1.5, 1.0]
eye_size: list[float] = [3.0, 1.25, 1.0]
shine_size: list[float] = [1.0, 0.5, 1.0]


def main() -> None:
    """The entrypoint of my scene."""
    draw_oval(right_leg, -250, 0, leg_size, leg_color)
    draw_oval(left_leg, -50, 0, leg_size, leg_color)
    draw_body(kirby, -150, -50, 150, body_color)
    draw_body(kirby, -20, 100, 50, body_color)
    draw_body(kirby, -300, 80, 50, body_color)
    draw_body(kirby, -125, -10, 70, mouth_color)
    draw_oval(right_blush, -225, 130, blush_size, blush_color)
    draw_oval(left_blush, -50, 130, blush_size, blush_color)
    draw_oval(right_eye, -170, 170, eye_size, eye_color)
    draw_oval(left_eye, -110, 170, eye_size, eye_color)
    draw_oval(right_shine, -170, 185, shine_size, shine_color)
    draw_oval(left_shine, -110, 185, shine_size, shine_color)
    draw_body(kirby, -140, 1, 45, tongue_color)
    i: int = 0
    side_length: float = 50.0
    while (i < 4):
        """Using the randint function to generate random x,y coordinates which will generate different positions for the stars."""
        """Using a while loop to call the draw_star function 4 times which would draw 4 stars in random positions."""
        x: float = randint(0, 300)
        y: float = randint(0, 200)
        draw_star(star, x, y, side_length)
        side_length = side_length * 0.60
        i = i + 1
    done()


def draw_star(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Using random integers for the x,y starting position, this function draws a star."""
    i: int = 0
    star.color(255, 234, 110)
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.fillcolor(255, 234, 110)
    star.begin_fill()
    while (i < 5):
        star.forward(length)
        star.right(120)
        star.forward(length)
        star.right(-48)
        i = i + 1
    star.end_fill()


def draw_body(a_turtle: Turtle, x: float, y: float, r: float, color: tuple[int, int, int]) -> None:
    """Using xy coordinates, a radius for the size of the circle, and a color, to create kirby's body as well as kirby's mouth."""
    kirby.color(color)
    kirby.penup()
    kirby.goto(x, y)
    kirby.pendown()
    kirby.fillcolor(color)
    kirby.begin_fill()
    kirby.circle(r)
    kirby.end_fill()


def draw_oval(a_turtle: Turtle, x: float, y: float, size: list[float], color: tuple[int, int, int]) -> None:
    """Using xy coordinates, the lenght, width, and pensize of the oval, and the color of the oval which can create kirby's legs, eyes, and eye details."""
    a_turtle.goto(x, y)
    a_turtle.color(color)
    a_turtle.fillcolor(color)
    a_turtle.begin_fill()
    a_turtle.shape("circle")
    a_turtle.shapesize(size[0], size[1], size[2]) 
    a_turtle.end_fill()


if __name__ == "__main__":
    main()