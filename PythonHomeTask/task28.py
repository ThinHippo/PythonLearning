# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
def sumnums(x,y):
    if y==0:
      return x
    else:
       step=int(y/abs(y))
       x+=step
       y-=step
       return sumnums(x,y)
print("Программа вычисляет сумму двух целых чисел A и B с помощью рекурсии.")
a=int(input("Введите число A: "))
b=int(input("Введите число B: "))
if abs(a)<abs(b):
   print(f"{a}+{b}={sumnums(b,a)}")
else:
   print(f"{a}+{b}={sumnums(a,b)}")