# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def involution(a,b):
    if b==0:
        return 1
    elif b<0:
        return round(1/a*involution(a,b+1),3)
    return a*involution(a,b-1)


a=float(input('Введите число А:'))
b=int(input('Введите целое число В:'))
print(f'A={a}; B={b} -> {involution(a,b)}')

