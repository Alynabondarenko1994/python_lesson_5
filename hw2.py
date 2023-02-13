# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4


def sum(a,b):
    if a==0 and b==0:
        return 0
    if a==1 and b==1:
        return 1+1
    if a==0:
        return 1+sum(0,b-1)
    if b==0:
        return 1+sum(a-1,0)
    return 1+1+sum(a-1,b-1)
   

a=int(input('Введите числа А:'))
while a<0  :
    a=int(input('Введите число больше 0 :' ))
b=int(input('Введите целое число В:'))
while b<0  :
    b=int(input('Введите число больше 0 :' ))
print(f'{a} + {b} = {sum(a,b)}')