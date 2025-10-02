correct_password = "truehardpasswordauthtokenrefreshaccesschatgptkeyopenaillmclaudegithubpassword"
password = input("Введите пароль: ") # получаем ввод пароля
if password == correct_password: # сравниваем пароли
    print("Доступ разрешен") # если true - доступ разрешен
else: # если пароли не совпадают
    print("Доступ запрещен") # доступ запрещен
