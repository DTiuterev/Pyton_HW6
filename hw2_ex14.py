#14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# number_str = input('Введите число, целое/дробное (разделитель дробной части . ): ')
# if "," in number_str:
#      print('Вы ввели некорректный разделитель дробной части')
#
# number_float = float(number_str)
# if number_float < 0:
#     number_float = -number_float
# number_str = str(number_float)
#
# sum_digits = 0
# for i in number_str:
#     if i != '.':
#         sum_digits += int(i)
# print(f'Сумма цифр = {sum_digits}')

number_str = (input('Введите число, целое/дробное (разделитель дробной части . ): '))
if "," in number_str:
    print('Вы ввели некорректный разделитель дробной части')
number_float = float(number_str)
if number_float < 0:
    number_float = -number_float
number_str = str(number_float)

sum_digits = sum(map(int, number_str.replace('.', '')))
print(f'Сумма цифр = {sum_digits}')

