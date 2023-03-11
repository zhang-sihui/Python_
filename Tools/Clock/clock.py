# @time: 2019/7/6 10:00

import turtle
import datetime


def move(distance):
    """悬空移动"""
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()


def create_hand(name, length):
    """创建表针turtle"""
    turtle.reset()
    move(-length * 0.01)
    turtle.begin_poly()
    turtle.forward(length * 1.01)
    turtle.end_poly()
    hand = turtle.get_poly()
    turtle.register_shape(name, hand)


def create_clock(radius):
    """创建时钟"""
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        move(radius)
        if i % 5 == 0:
            turtle.forward(20)
            move(-radius - 20)
        else:
            turtle.dot(5)
            move(-radius)
        turtle.right(6)


def get_weekday(today):
    """获取今天星期几"""
    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday',
            ]
    return week[today.weekday()]


def get_date(today):
    """获取今天日期"""
    return "%s年 %s月 %s日" % (today.year, today.month, today.day)


def start_tick(second_hand, minute_hand, hour_hand, printer):
    """动态显示表针"""
    today = datetime.datetime.today()
    second = today.second + today.microsecond * 1e-6
    minute = today.minute + second / 60
    hour = (today.hour + minute / 60) % 12
    # 设置朝向
    second_hand.setheading(6 * second)
    minute_hand.setheading(6 * minute)
    hour_hand.setheading(12 * hour)
    turtle.tracer(False)
    printer.forward(65)
    printer.write(get_weekday(today), align='center', font=('Courier', 14, 'bold'))
    printer.forward(120)
    printer.write('12', align='center', font=('Courier', 14, 'bold'))
    printer.back(250)
    printer.write(get_date(today), align='center', font=('Courier', 14, 'bold'))
    printer.back(145)
    printer.write('6', align='center', font=('Courier', 14, 'bold'))
    printer.home()
    printer.right(92.5)
    printer.forward(200)
    printer.write('3', align='center', font=('Courier', 14, 'bold'))
    printer.left(2.5)
    printer.back(400)
    printer.write('9', align='center', font=('Courier', 14, 'bold'))
    printer.home()
    turtle.tracer(True)
    # 100ms调用一次
    turtle.ontimer(lambda: start_tick(second_hand, minute_hand, hour_hand, printer), 100)


def start():
    """开始运行时钟"""
    # 不显示绘制时钟过程
    turtle.tracer(False)
    turtle.mode('logo')
    create_hand('second_hand', 150)
    create_hand('minute_hand', 125)
    create_hand('hour_hand', 85)
    # 秒，分，时
    second_hand = turtle.Turtle()
    second_hand.shape('second_hand')
    minute_hand = turtle.Turtle()
    minute_hand.shape('minute_hand')
    hour_hand = turtle.Turtle()
    hour_hand.shape('hour_hand')
    for hand in [second_hand, minute_hand, hour_hand]:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 打印日期文字
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()
    create_clock(160)
    # 开始显示轨迹
    turtle.tracer(True)
    start_tick(second_hand, minute_hand, hour_hand, printer)
    turtle.mainloop()


if __name__ == '__main__':
    start()
