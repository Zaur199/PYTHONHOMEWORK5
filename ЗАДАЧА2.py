#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота

#b) Подумайте как наделить бота ""интеллектом""

from random import randint
print("*" * 9, "Играют 2 игрока", "*" * 9)
igrok1 = input("Введите имя первого игрока: ")
igrok2 = input("Введите имя второго игрока: ")
result = int(input("Введите количество конфет на столе: "))
counter1 = 0 
counter2 = 0
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {igrok1}")
else:
    print(f"Первый ходит {igrok2}")

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, result):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {result} конфет.")

while result > 28:
    if flag:
        k = input_dat(igrok1)
        counter1 += k
        result -= k
        flag = False
        p_print(igrok1, k, counter1, result)
    else:
        k = input_dat(igrok2)
        counter2 += k
        result -= k
        flag = True
        p_print(igrok2, k, counter2, result)

if flag:
    print(f"Выиграл {igrok1}")
else:
    print(f"Выиграл {igrok2}")