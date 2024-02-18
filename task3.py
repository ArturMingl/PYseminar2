"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""
import fractions
import math

print('Введите две дроби вида “a/b”')
fract_1 = [int(n) for n in input('Первая дробь: ').split('/')]
fract_2 = [int(n) for n in input('Вторая дробь: ').split('/')]
f1 = fractions.Fraction(fract_1[0], fract_1[1])
f2 = fractions.Fraction(fract_2[0], fract_2[1])

# Сумма дробей
fract_lcm = math.lcm(fract_1[1], fract_2[1])  # ищем НОК
numerator_1 = int(fract_lcm / fract_1[1] * fract_1[0])
numerator_2 = int(fract_lcm / fract_2[1] * fract_2[0])
numerator_sum = numerator_1 + numerator_2
fract_gcd = math.gcd(numerator_sum, int(fract_lcm)) # ищем НОД и сокращаем дробь
fract_sum = str(int(numerator_sum / fract_gcd)) + '/' + str(int(fract_lcm / fract_gcd))

# Произведение дробей
numerator = fract_1[0] * fract_2[0]
denominator = fract_1[1] * fract_2[1]
fract_gcd = math.gcd(numerator, denominator) # ищем НОД и сокращаем дробь
fract_mult = str(int(numerator / fract_gcd)) + '/' + str((int(denominator / fract_gcd)))

print(f'Ожидаемый результат сложения:  {f1 + f2}')
print(f'Полученный результат сложения: {fract_sum}')

print(f'Ожидаемый результат умножения:  {f1 * f2}')
print(f'Полученный результат умножения: {fract_mult}')
