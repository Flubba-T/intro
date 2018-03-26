import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

len = 100

def snowflake(order, size):
    t.tracer(10, 10)
    if order > 0:
        for degree in [60, -120, 60, 0]:
            snowflake(size/3, order-1)
            t.lt(degree)
    else:
        t.fd(size)
t.pu()
t.setpos(-350,225)
t.pd()
snowflake(5, len)
t.rt(120)
snowflake(5,len)
t.rt(120)
snowflake(5,len)
wn.exitonclick()
