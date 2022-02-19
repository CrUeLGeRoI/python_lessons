# 1
# def message(name):
#     print(f"Hello, {name}!")
#
#
# message("Gleb")
# 2
# def exercise(msg, n):
#     count = 0
#     while count < n:
#         print(msg)
#         count += 1
#
#
# exercise("Lol", 3)
# 3
# def exercise(msg, n):
#     count = 0
#     while count < n:
#         print(msg)
#         count += 1
#
#
# exercise("Lol", 3)
# 4

# 5

# 6
# def max(a, b):
#     if a > b:
#         return a
#     elif a == b:
#         return "equal"
#     else:
#         return b
#
#
# print(max(8, 100))
# print(max(1, 0.5))
# print(max(0.05, 0.05))
# 7
# def max(a, b, c):
#     if b > a and b > c:
#         return b
#     elif c > a and c > b:
#         return c
#     else:
#         return a

# 8
# def triangle(x, y, z):
#     if x + y > z and x + z > y and y + z > x:
#         print("Это треугольник")
#     else:
#         print("Это не треугольник")
#
#
# a = int(input("1 сторона: "))
# b = int(input("2 сторона: "))
# c = int(input("3 сторона: "))
# print(triangle(a, b, c))
# 9
# def merge(a, b):
#     print(f"{a} {b}")
#
#
# merge("Aboba", "Abobus")
# 10
# def calc(a, b, c):
#     if c == "+":
#         return a + b
#     elif c == "*":
#         return a * b
#     elif c == "/":
#         return a / b
#     elif c == "-":
#         return a - b
#     else:
#         return "Unknown operation"
#
#
# x = int(input("1 num: "))
# y = int(input("2 num: "))
# z = input("Operation(+ - * /): ")
# print(round(calc(x, y, z), 2))

# 11
# def html(tag, a):
#     return f"<{tag}>{a}</{tag}>"
#
#
# print(html(input("Tag: "), input("Info: ")))
# 12
# def season(a):
#     if 3 <= a <= 5:
#         print("Spring")
#     elif 6 <= a <= 8:
#         print("Summer")
#     elif 9 <= a <= 11:
#         print("Autumn")
#     elif a == 12 or 1 <= a <= 2:
#         print("Winter")
#
#
# season(3)
# 13
# def gystogram(a):
#     for i in a:
#         print("*" * i)
#
#
# gystogram([2, 4, 100, 8])

# 14
# def num(a):
#     if a % 2 == 0:
#         print("Число чётное")
#     else:
#         print("Число не чётное")
#
#
# num(10)
# 15
# def first_and_last_child(a):
#     b = [a[0], a[-1]]
#     return b
#
#
# print(first_and_last_child([1, 2, 3, 4, 5, 6, 7, 8]))
# 16
# def factorial(a):
#     z = 1
#     for i in range(1, a + 1):
#         z *= i
#     return z
#
#
# print(factorial(10000))
# 17
import math


def triangle(a, b, c):
    print("Площадь треугольника считается через полупериметр")
    p = (a + b + c) / 2
    s = round(math.sqrt(p * (p - a) * (p - c) * (p - c)), 2)
    print(s)


def check_triangle(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False


def circle(r):
    print("Площадь круга считается так: число пи * радиус круга в квадрате")
    s = round(math.pi, 2) * r ** 2
    print(s)


def rectangle(a, b):
    print("Площадь прямоугольника считается так: 1 сторона * 2 сторона")
    s = a * b
    print(s)


def find_area_of_figure(figure):
    if figure == "circle":
        circle(int(input("Enter radius: ")))
    elif figure == "triangle":
        a = int(input("1 сторона: "))
        b = int(input("2 сторона: "))
        c = int(input("3 сторона: "))
        if check_triangle(a, b, c):
            triangle(a, b, c)
        else:
            print("Такой треугольник не существует")
    elif figure == "rectangle":
        rectangle(int(input("Enter 1 side: ")), int(input("Enter 2 side: ")))


find_area_of_figure(input("Enter figure(triangle, circle, rectangle): "))
