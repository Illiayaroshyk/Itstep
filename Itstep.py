import turtle
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)
def snowflake(t, order, size):
    for i in range(3):
        koch(t, order, size)
        t.right(120)
def draw_snowflake():
                t = turtle.Turtle()
                t.speed(0)
                snowflake(t, 3, 200)
                turtle.done()
draw_snowflake()