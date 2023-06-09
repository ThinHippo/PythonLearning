# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import random
print("Программа считает максимальное количество ягод, которые можно собрать с трёх соседних кустов.")
n=int(input("Укажите количество кустов: "))
berry=[]
minVal=10
maxVal=50
for i in range(n):
    berry.append(random.randint(minVal,maxVal))
j=len(berry)-1
fullbasket=[]
while j>=0:
    fullbasket.append(berry[j]+berry[j-1]+berry[j-2])
    j-=1
print(f"Количество ягод на кустах: {berry}")
print(f"Максимальный сбор с трёх смежных кустов составит: {max(fullbasket)}")

