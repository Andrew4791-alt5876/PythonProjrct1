pin_correct = "0000"
attempts = 3
count_attempts = attempts
while count_attempts > 0:
    pin = input("Введите пин код из четырех чисел: ")
    if len(pin) != 4 and count_attempts <= attempts:
        count_attempts += 1
        print("В пин коде четыре цифры! будьте внимательней!")
    if pin == pin_correct:
        count_attempts -= 1
        print("Добро пожаловать!")
        break
    count_attempts -= 1
else:
    print("Ваша карта заблокированна")
