# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
import random
print("Программа находит самый близкий по величине элемент к заданному числу X в списке из N элементов.")
N=int(input("Укажите размер списка N="))
X=int(input("Введите искомое значение X="))
minValue=-10
maxValue=10
xDiff=0
item=0
A=[]
for i in range(N):    
    A.append(random.randint(minValue,maxValue))
    if i==0:xDiff=abs(A[i]-X)
    if abs(A[i]-X)<xDiff:
       xDiff=abs(A[i]-X)
       item=i
    print(A[i], end=" ")
print(f"\nСамый близкий по величине элемент к заданному числу {X} A[{item}]={A[item]}")