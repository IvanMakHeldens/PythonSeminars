# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


pvp_or_bot = int(input("Чтобы играть вдвоём введите 2. Чтобы играть против бота введите 1  "))
if pvp_or_bot == 2:
    print("Игра началась")
    pool = int(input("Введите общее количество конфет: "))
    count = 1
    while pool > 0:
        if count == 1:
            move1 = int(input("Игрок 1, сколько конфет берёте? Введите число: "))
            if move1 < 1 or move1 > 28:
                print("Возьмите от 1 до 28 конфет!")
                move1 = int(input("Игрок 1, сколько конфет берёте? Введите число: "))
                if move1 < 1 or move1 > 28:
                    print("ХВАТИТ ЖУЛЬНИЧАТЬ! ИГРА ОКОНЧЕНА! Игрок 2 забирает все конфеты!")
                    exit()
                elif move1 > pool:
                    print (f"Осталось {pool} конфет! Возьмите от 1 до {pool} конфет!")
                else:
                    pool -= move1
                    print (f"Осталось {pool} конфет")
                    count -= 1
            elif move1 > pool:
                print (f"Осталось {pool} конфет! Возьмите от 1 до {pool} конфет!")
            else:
                pool -= move1
                print (f"Осталось {pool} конфет")
                count -= 1
        elif count == 0:
            move2 = int(input("Игрок 2, сколько конфет берёте? Введите число: "))
            if move2 < 1 or move2 > 28:
                print("Возьмите от 1 до 28 конфет!")
                move2 = int(input("Игрок 2, сколько конфет берёте? Введите число: "))
                if move2 < 1 or move2 > 28:
                    print("ХВАТИТ ЖУЛЬНИЧАТЬ! ИГРА ОКОНЧЕНА! Игрок 1 забирает все конфеты!")
                    exit()
                elif move1 > pool:
                    print (f"Осталось {pool} конфет! Возьмите от 1 до {pool} конфет!")
                else:
                    pool -= move1
                    print (f"Осталось {pool} конфет")
                    count += 1
            elif move2 > pool:
                print (f"Осталось {pool} конфет! Возьмите от 1 до {pool} конфет!")
            else:
                pool -= move2
                print (f"Осталось {pool} конфет")
                count += 1
    if count == 0:
        print("Игрок 1 побеждает и забирает все конфеты!")
    else:
        print("Игрок 2 побеждает и забирает все конфеты!")

elif pvp_or_bot == 1:
    import random
    player_name = input("Как звать? Введите имя: ")
    print("Игра началась")
    pool = int(input("Введите общее количество конфет: "))

    count = random.randint(0, 1)
    if count == 0:
        print("Первым ходит бот, для Вас без шансов :)")
    else:
        print(f"{player_name}, Вы ходите первым, шанс победить есть, но нужно думать!")
    while pool > 0:
        if count == 1:
            move1 = int(input(f"{player_name}, сколько конфет берёте? Введите число: "))
            if move1 < 1 or move1 > 28:
                print("Возьмите от 1 до 28 конфет!")
                move1 = int(input(f"{player_name}, сколько конфет берёте? Введите число: "))
                if move1 < 1 or move1 > 28:
                    print("ХВАТИТ ЖУЛЬНИЧАТЬ! ИГРА ОКОНЧЕНА! Бот забирает все конфеты!")
                    exit()
                elif move1 > pool:
                    print (f"Осталось {pool} конфет! Возьмите от 1 до {pool} конфет!")
                else:
                    pool -= move1
                    print (f"Осталось {pool} конфет")
                    count -= 1
            elif move1 > pool:
                print (f"Осталось {pool} конфет! Возьмите от 1 до {pool} конфет!")
            else:
                pool -= move1
                print (f"Осталось {pool} конфет")
                count -= 1
        elif count == 0:
            if pool > 28:
                if pool % 29 == 0:
                    move2 = random.randint(1, 28)
                else:
                    move2 = pool % 29
                print(f"Ход компьютера: бот забрал {move2} конфет")
            else:
                move2 = pool
                print(f"Ход компьютера: бот забрал {move2} конфет")
            pool -= move2
            print(f"Осталось {pool} конфет")
            count += 1
    if count == 0:
        print(f"{player_name} побеждает и забирает все конфеты!")
    else:
        print("Компьютер побеждает и забирает все конфеты!")
else:
    print("неправильно набран номер the number you have dialed is not in service try again later")