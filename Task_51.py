# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

S = 2021
print(f'Количество конфет: {S}')

# Человек с человеком

# from random import randint
# Name1 = str(input("Введите имя первого игрока: "))
# Name2 = str(input("Введите имя второго игрока: "))
# A = randint(1, 6)
# B = randint(1, 6)
# print(f'{Name1} выкинул число: {A}')
# print(f'{Name2} выкинул число: {B}')
# while A == B:
#     print('Нужно повторить вбрасывание кубиков')
#     break
# if A > B: print(f'{Name1} ходит первым')    
# if A < B: print(f'{Name2} ходит первым') 

 
# while S > 0:
#     s1 = int(input("Введите сколько конфет взял первый игрок: "))
#     if s1 > 28:
#         print('Нельзя вводить число больше 28')
#         s1 = int(input("Введите сколько конфет взял первый игрок: "))
#         S = S- s1
#         print(f'Остаток конфет: {S}')
#         if S == 0:
#             print('Все конфеты достаются первому игроку')    
#     else:
#         S = S- s1
#         print(f'Остаток конфет: {S}')
#         if S == 0:
#             print('Все конфеты достаются первому игроку')
#     s2 = int(input("Введите сколько конфет взял второй игрок: "))
#     if s2 > 28:
#         print('Нельзя вводить число больше 28')
#         s2 = int(input("Введите сколько конфет взял второй игрок: "))
#         S = S - s2
#         print(f'Остаток конфет: {S}')
#         if S == 0:
#             print('Все конфеты достаются второму игроку')
#     else:   
#         S = S - s2
#         print(f'Остаток конфет: {S}')
#         if S == 0:
#             print('Все конфеты достаются второму игроку')

#------------------------------------------------------------------------------
# Человек - Бот

# from random import randint
# while S > 0:
#     s1 = int(input("Введите сколько конфет взял первый игрок: "))
#     if s1 > 28:
#         print('Нельзя вводить число больше 28')
#         s1 = int(input("Введите сколько конфет взял первый игрок: "))
#         S = S- s1
#         print(f'Остаток конфет: {S}')
#         if S == 0:
#             print('Все конфеты достаются первому игроку')    
#     else:
#         S = S- s1
#         print(f'Остаток конфет: {S}')
#         if S == 0:
#             print('Все конфеты достаются первому игроку')
#     s2 = randint(1, 29)
#     if s2 > S:
#         s2 = S
#         print(f'Компьтер берет {s2} конфет')
#         S = S - s2
#         print('Все конфеты достаются компьютеру')
#     else:
#         print(f'Компьтер берет {s2} конфет')
#         S = S - s2
#         print(f'Остаток конфет: {S}')
#         if S == 0:
#             print('Все конфеты достаются компьютеру')

# -------------------------------------------------------------------------

# Человек - Бот(обученный)

from random import randint
while S > 0:
    s1 = int(input("Введите сколько конфет взял первый игрок: "))
    if s1 > 28:
        print('Нельзя вводить число больше 28')
        s1 = int(input("Введите сколько конфет взял первый игрок: "))
        S = S- s1
        print(f'Остаток конфет: {S}')
        if S == 0:
            print('Все конфеты достаются первому игроку')    
    else:
        S = S- s1
        print(f'Остаток конфет: {S}')
        if S == 0:
            print('Все конфеты достаются первому игроку')
    s2 = S % 29
    if s2 > S:
        s2 = S
        print(f'Компьтер берет {s2} конфет')
        S = S - s2
        print('Все конфеты достаются компьютеру')
    else:
        print(f'Компьтер берет {s2} конфет')
        S = S - s2
        print(f'Остаток конфет: {S}')
        if S == 0:
            print('Все конфеты достаются компьютеру')

