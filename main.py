import turtle
import math
import random

# -------------------------
# SCREEN
# -------------------------

screen = turtle.Screen()
screen.bgcolor("#1a0514")
screen.title("For You <3")
screen.setup(width=800, height=800)

# -------------------------
# TURTLE
# -------------------------

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

WORD = ""
FONT = ("Arial", 8, "bold")


# -------------------------
# DRAW PETAL
# -------------------------

def draw_petal(base, base_angle, length, width, color, points=26):

    t.color(color)

    bx, by = base

    cos_a = math.cos(base_angle)
    sin_a = math.sin(base_angle)

    # Start at base
    t.penup()
    t.goto(bx, by)
    t.pendown()

    # Draw petal
    for i in range(points + 1):

        theta = i * math.pi / points

        out = length * math.sin(theta)
        side = width * math.sin(theta) * math.cos(theta)

        rx = out * cos_a - side * sin_a
        ry = out * sin_a + side * cos_a

        t.goto(
            bx + rx,
            by + ry
        )

    # Close the petal
    t.goto(bx, by)

    # Write "my love" in the petal
    t.penup()

    center_x = bx + (length * 0.45) * cos_a
    center_y = by + (length * 0.45) * sin_a

    t.goto(center_x, center_y)

    t.color(color)

    t.write(
        WORD,
        align="center",
        font=FONT
    )


# -------------------------
# DRAW LEAF
# -------------------------

def draw_leaf(base, angle_deg, length, width):

    draw_petal(
        base,
        math.radians(angle_deg),
        length,
        width,
        "#2e8b57",
        points=22
    )


# -------------------------
# FLOWER RINGS
# -------------------------

rings = [

    {
        "radius": 0,
        "count": 4,
        "length": 40,
        "width": 15,
        "color": "#ffe6f2",
        "offset": 45
    },

    {
        "radius": 10,
        "count": 5,
        "length": 50,
        "width": 25,
        "color": "#ffb3d9",
        "offset": 0
    },

    {
        "radius": 20,
        "count": 7,
        "length": 70,
        "width": 35,
        "color": "#ff66b2",
        "offset": 30
    },

    {
        "radius": 30,
        "count": 9,
        "length": 90,
        "width": 45,
        "color": "#ff1493",
        "offset": 15
    },

    {
        "radius": 40,
        "count": 12,
        "length": 110,
        "width": 55,
        "color": "#c71585",
        "offset": 0
    }

]


# -------------------------
# STEM
# -------------------------

t.goto(0, -30)

t.setheading(260)

t.pendown()

t.color("#2e8b57")

t.pensize(4)

t.circle(250, 25)


# -------------------------
# FIRST LEAF
# -------------------------

pos1 = t.position()
head1 = t.heading()

t.pensize(1)

draw_leaf(
    base=pos1,
    angle_deg=160,
    length=50,
    width=25
)

t.penup()

t.goto(pos1)

t.setheading(head1)

t.pendown()


# -------------------------
# SECOND STEM SECTION
# -------------------------

t.color("#2e8b57")

t.pensize(4)

t.circle(250, 20)


# -------------------------
# SECOND LEAF
# -------------------------

pos2 = t.position()
head2 = t.heading()

t.pensize(1)

draw_leaf(
    base=pos2,
    angle_deg=20,
    length=55,
    width=28
)

t.penup()

t.goto(pos2)

t.setheading(head2)

t.pendown()


# -------------------------
# FINISH STEM
# -------------------------

t.color("#2e8b57")

t.pensize(4)

t.circle(250, 30)

t.penup()

t.pensize(1)


# -------------------------
# FLOWER PETALS
# -------------------------

for ring in rings:

    for i in range(ring["count"]):

        angle = (
            (360 / ring["count"]) * i
            + ring["offset"]
        )

        base_x = (
            ring["radius"]
            * math.cos(math.radians(angle))
        )

        base_y = (
            ring["radius"]
            * math.sin(math.radians(angle))
        )

        draw_petal(
            base=(base_x, base_y),
            base_angle=math.radians(angle),
            length=ring["length"],
            width=ring["width"],
            color=ring["color"]
        )


# -------------------------
# LITTLE HEARTS
# -------------------------

t.color("#ff99cc")

for _ in range(12):

    x = random.randint(-250, 250)
    y = random.randint(-250, 250)

    if math.hypot(x, y) > 130:

        t.goto(x, y)

        t.write(
            "<3",
            align="center",
            font=("Courier", 10, "bold")
        )


# -------------------------
# BOTTOM MESSAGE
# -------------------------

t.goto(0, -320)

t.color("white")

t.write(
    "Click anywhere to close",
    align="center",
    font=("Arial", 10, "italic")
)


# -------------------------
# KEEP WINDOW OPEN
# -------------------------

screen.exitonclick()