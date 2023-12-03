import turtle
import random

# setposition() - координаты
# speed() - скорость
# penup() - подымаем перо
# pendown() - опускаем перо
# begin_fill() - начало заливки
# end_fill() - конец заливки
# color() - цвета

turtle.speed(0)

window = turtle.Screen()
window.bgcolor('black')
# Координаты окна
n_x = 1000
m_y = 700
window.setup(n_x, m_y)

star_j = turtle.Turtle()  # Звезды
house_walls = turtle.Turtle()  # Стены дома
house_door = turtle.Turtle()  # Дверь дома
house_windows = turtle.Turtle()  # Окна дома
house_roof = turtle.Turtle()  # Крыша дома
land = turtle.Turtle()  # Земля

land.speed(0)

land.color('green')
land.up()
land.setposition(-(n_x // 2), -(m_y // 2))
land.down()


def lend_fill():
    land.begin_fill()
    for i in range(2):
        land.forward(n_x)
        land.left(90)
        land.forward(m_y // 4)
        land.left(90)
    land.end_fill()


lend_fill()

house_walls.speed(0)

house_walls.color('red')
house_walls.up()
house_walls.setposition(-(n_x // 2 - 350), -(m_y // 4))
house_walls.down()


def house_walls_fill():
    house_walls.begin_fill()
    for i in range(2):
        house_walls.forward(n_x // 4)
        house_walls.left(90)
        house_walls.forward(m_y // 4)
        house_walls.left(90)
    house_walls.end_fill()
    house_walls.penup()


house_walls_fill()

house_door.speed(0)
house_door.color("brown")
house_door.up()
house_door.setposition(-((n_x // 2 - 300) // 3), -(m_y // 4))
house_door.down()


def house_door_fill():
    house_door.begin_fill()
    for i in range(2):
        house_door.forward(n_x // 15)
        house_door.left(90)
        house_door.forward(m_y // 9)
        house_door.left(90)
    house_door.end_fill()
    house_door.up()
    house_door.setposition(-((n_x // 2 - 300) // 3 - 33), -(m_y // 6))
    house_door.down()
    house_door.color('blue')
    house_door.begin_fill()
    house_door.circle(3)
    house_door.end_fill()

    house_door.up()
    house_door.setposition(-((n_x // 2 - 300) // 3 - 4), -(m_y // 5))
    house_door.down()
    house_door.color('yellow')
    for i in range(5):
        house_door.forward(5)
        angle = 5 // 2 * 360 / 5
        house_door.left(angle)
    house_door.end_fill()


house_door_fill()

house_windows.speed(0)
house_windows.color('black')
house_windows.fillcolor('white')
house_windows.up()
hw_pos_1 = [-(n_x // 2 - 370), -(m_y // 9)]
hw_pos_2 = [-(n_x // 2 - 540), -(m_y // 9)]
house_windows.setposition(hw_pos_1[0], hw_pos_1[1])


def house_windows_fill():
    house_windows.begin_fill()
    for i in range(2):
        house_windows.forward(40)
        house_windows.left(90)
        house_windows.forward(40)
        house_windows.left(90)
    house_windows.end_fill()
    house_windows.down()
    house_windows.color('black')
    house_windows.forward(20)
    house_windows.left(90)
    house_windows.forward(40)
    house_windows.right(90)
    house_windows.forward(20)
    house_windows.right(90)
    house_windows.forward(20)
    house_windows.right(90)
    house_windows.forward(40)
    house_windows.left(90)
    house_windows.forward(20)
    house_windows.left(90)
    house_windows.forward(40)
    house_windows.left(90)
    house_windows.forward(40)
    house_windows.left(90)
    house_windows.forward(40)
    house_windows.left(90)
    house_windows.forward(20)


house_windows_fill()
house_windows.up()
house_windows.setposition(hw_pos_2[0], hw_pos_2[1])
house_windows.down()
house_windows.left(90)
house_windows.color('black')
house_windows.fillcolor('white')
house_windows_fill()
house_windows.up()

house_roof.color('purple')
house_roof.begin_fill()
house_roof.backward(150)
h = 218
a = (2 * h) / (3 ** 0.5)
house_roof.speed(0)
house_roof.left(60)
house_roof.forward(a)
house_roof.right(120)
house_roof.forward(a)
house_roof.right(120)
house_roof.forward(a)
house_roof.end_fill()


# Функция по рисованию звезд
def star_fill(n, length):
    star_j.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            star_j.forward(length)
            angle = n // 2 * 360 / n
            star_j.left(angle)
    star_j.end_fill()


star_j.speed(0)
star_j.color('yellow')
count_of_stars = int(input("Введите количество звёздочек: "))


for i in range(count_of_stars // 3):
    x = random.randint(-(n_x // 2 - 30), (n_x // 2 - 30))
    if -195 < x < 195:
        y = random.randint(100+round((200*100 - abs(x)*100)/200), round(m_y/2))+2
    else:
        y = random.randint(m_y // 2 - 100, m_y // 2)
    star_j.up()
    star_j.setposition(x, y)
    star_j.down()
    size = random.randint(5, 10)
    star_fill(5, size)


for i in range(count_of_stars // 3):
    x = random.randint(-(n_x // 2), -(n_x // 2 - 330))
    y = random.randint(-(m_y // 2 - 200), m_y // 2)
    star_j.up()
    star_j.setposition(x, y)
    star_j.down()
    size = random.randint(5, 10)
    star_fill(5, size)

for i in range(count_of_stars // 3):
    x = random.randint(n_x // 2 - 400, n_x // 2)
    y = random.randint(-(m_y // 2 - 200), m_y // 2)
    star_j.up()
    star_j.setposition(x, y)
    star_j.down()
    size = random.randint(5, 10)
    star_fill(5, size)

house_windows.ht()
house_walls.ht()
house_door.ht()
house_roof.ht()
land.ht()
star_j.ht()

turtle.done()  # Рисунок закончен
turtle.exitonclick()  # Выход при нажатии мышкой в окне Turtle
