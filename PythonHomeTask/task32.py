# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#(т.е. не меньше заданного минимума и не больше заданного максимума)
import random
def appendList(n,left,right):
    myList=[]
    for i in range(n):
        myList.append(random.randint(left,right))
    return myList

def getIndexInLimitValue(L,down,up):
    tmp=up
    if up<down:
      up=down
      down=tmp  
    resultList=[]
    for i in range(len(L)):
        if down <=L[i]<=up:
            resultList.append (i)
    return resultList

print("Программа выводит индексы элементов списка, значения которых принадлежат заданному диапазону.")
listLen=20
minValue=-25
maxValue=50
testList=appendList(listLen,minValue,maxValue)
print(f"Исходный массив (список): {testList}")
minLimit=int(input("Задайте минимум: "))
maxLimit=int(input("Задайте максимум: "))
print(f"Результат: {getIndexInLimitValue(testList,minLimit,maxLimit)}")