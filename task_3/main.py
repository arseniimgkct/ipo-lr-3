day = int(input("Введите день числом: ")) # получаем день
month = int(input("Введите месяц числом: ")) # получаем месяц

if day <= 0 or day > 31:
    print("Некорректный день")
    exit()

if month >= 3 and month < 6: # если месяц в диапазоне от 3 до 6, то это весна
    if ((month == 3 or month == 5) and day > 31) or (month == 4 and day > 30):
            print("Некорректный день")
    else:
        print("Весна") # выводим весну
elif month >= 6 and month < 9: # если месяц в диапазоне от 6 до 9, то это лето
    if ((month == 7 or month == 8) and day > 31) or (month == 6 and day > 30):
            print("Некорректный день")
    else:
        print("Лето") # выводим лето
elif month >= 9 and month < 12: # если месяц в диапазоне от 9 до 12, то это осень
    if ((month == 9 or month == 11) and day > 30) or (month == 10 and day > 31):
        print("Некорректный день")
    else:
        print("Осень") # выводим осень
elif month == 12 or month < 3: # если месяц равен 12 или меньше 3, то это зима
    if ((month == 12 or month == 1) and day > 31) or (month == 2 and day > 28):
        print("Некорректный день")
    else:
        print("Зима") # выводим зиму
else: # обрабатываем невалидные данные
    print("Некорректный месяц") # выводим