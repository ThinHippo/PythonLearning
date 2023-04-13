#Задача 2: Найдите сумму цифр трехзначного числа.
#Пример:
#   123 -> 6 (1 + 2 + 3)
#   100 -> 1 (1 + 0 + 0)
import random
print("Программа выводит сумму цифр трёхзначного числа.")
n=random.randint(100,999)
print(f"Число n={n}")
sumResult=0
strResult=""
for i in str(n):
    sumResult+=int(i)
    strResult=strResult+i+"+"
if strResult.endswith("+"):
  strResult=strResult[:len(strResult)-1]
print (f"{strResult}={sumResult}")