"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

num = int(input('Введите число: '))
print(f'Вы ввели: {num} \n Ожидаемый результат:  {hex(num)}')
result = ''
HEX = 16
hex_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

while num > 0:
    res = num % HEX
    if res in hex_dict:
        res = hex_dict[res]
    result = str(res) + result
    num = num // HEX
result = '0x' + result

print(f' Полученный результат: {result}')

