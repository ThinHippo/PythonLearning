#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#Пример:
#  6 -> 1  4  1
#  24 -> 4  16  4
#  60 -> 10  40  10
import random
print("Программа рассчитывает количество птичек, изготовленных каждым ребёнком с учётом заданной производительности.")
peterOutput=1
sergeOutput=1
kateOutput=2*(peterOutput+sergeOutput)
totalOutput=kateOutput+peterOutput+sergeOutput
realOutput=1
while (realOutput%totalOutput != 0):
    realOutput=random.randint(1,100)
peterOutput=int(realOutput/totalOutput)
sergeOutput=peterOutput
kateOutput=int(realOutput-peterOutput-sergeOutput)
print(f"Всего изготовлено {realOutput} журавликов")
print(f"\tКатя сделала {kateOutput} журавликов\n\tПетя сделал {peterOutput} журавликов\n\tСерёжа сделал {sergeOutput} журавликов")