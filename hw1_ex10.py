# import math
#
# x_A = int(input('Введите координату x точки А: '))
# y_A = int(input('Введите координату y точки А: '))
# x_B = int(input('Введите координату x точки B: '))
# y_B = int(input('Введите координату y точки B: '))
#
# distance = round(math.sqrt((x_B - x_A)**2 + (y_B - y_A)**2), 2)
# print(distance)

from functools import reduce
a = list(map(int, input('Введите координаты x и y точки A, через пробел: ').split()))
b = list(map(int, input('Введите координаты x и y точки B, через пробел: ').split()))
def distance(a, b):
     dist = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(a, b))))
     return round(dist, 2)
print(distance())
