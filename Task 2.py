# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
from msilib import sequence
n = int(input('Введите число n '))
num = [round((1+1/i)**i,2) for i in range (1, n+1)]
print(f'Для n = {n} -> {num}')
print(round(sum(num),2))