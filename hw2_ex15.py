#15. Напишите программу, которая принимает на вход число N и выдает набор произведений целых чисел от 1 до N.
# n = int(input('Введите целое число N, я выведу набор произведений чисел от 1 до N: '))
# if n > 0:
#     i = 1
#     result = 1
#     numbers = []
#     while i <= n:
#         result = result * i
#         numbers.append(result)
#         i += 1
#     print(numbers)
# else:
#     print('Вы ввели отрицательное число или 0. Между 1 и этим числом будет умножение на 0 и результат всех вычислений всегда будет = 0 ')

from math import factorial
n = int(input('Введите целое число N, я выведу набор произведений чисел от 1 до N: '))
if n > 0:
    print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x - 1), list(range(1, n + 1)))))
else:
    print('Вы ввели отрицательное число или 0. Между 1 и этим числом будет умножение на 0 и результат всех вычислений всегда будет = 0 ')
