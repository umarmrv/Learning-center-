import random
cards = {}
def register_card():
    bank = input("Введите название банка: ")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")
    pin = input("Введите PIN-код: ")
   
    card_data = {
        "bank": bank,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "pin": pin
    }
   
    cards[phone_number] = card_data
    print("Карта зарегистрирована.")


def atm_system():
    phone_number = input("Введите номер телефона для доступа: ")
    if phone_number not in cards:
        print("Банк не найден.")
        return
   
    pin = input("Введите PIN-код: ")
    if cards[phone_number]["pin"] != pin:
        print("Неверный PIN-код.")
        return
   
    print("Доступ к системе получен.")
    withdraw_money()


def withdraw_money():
    available_amounts = [100, 200, 500, 1000, 2000]
    print(f"Доступные суммы для снятия: {available_amounts}")
   
    while True:
        amount = int(input("Введите сумму для снятия: "))
        if amount in available_amounts:
            print(f"Выдано: {amount} рублей.")
            break
        else:
            print("Сумма недоступна. Пожалуйста, выберите другую сумму.")


def main():
    while True:
        action = input("Выберите действие: 1 - регистрацию, 2 - доступ к банкомату, 0 - выход: ")
        if action == "1":
            register_card()
        elif action == "2":
            atm_system()
        elif action == "0":
            print("Выход из системы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main