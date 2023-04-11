import re


# task 1. Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
# (наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном, до якого відноситься
# ця дата ("літо", "осінь", "зима", "весна")

def season():
    """
    Function that returns a name of a season. User should enter the date in specific format: "\d\d.\d\d"
    :return:name of a season
    :rtype: str
    """
    while True:
        date = input(str("Enter the date in format [day].[month] (dd.mm): "))
        user_date = re.match("\d\d.\d\d", date)
        is_match = bool(user_date)

        if is_match == False:
            continue
        if is_match == True:
            break

    month = date[3:]
    user_date = date[:2]

    if int(month) > 12 or int(month) < 0:
        print("This month doesn't exist")
        return

    if int(user_date) > 31 or int(user_date) < 0:
        print("This date doesn't exist")
        return

    if month.startswith("0"):
        month = int(month[1:])
    else:
        month = int(month)

    if month == 1 or month == 2 or month == 12:
        print("winter")
    elif month == 3 or month == 4 or month == 5:
        print("spring")
    elif month == 6 or month == 7 or month == 8:
        print("summer")
    elif month == 9 or month == 10 or month == 11:
        print("autumn")


season()


# task 2. Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий, який відповідає за
# операцію між ними (+ - / *). Функція повинна повертати значення відповідної операції (додавання, віднімання, ділення,
# множення), інші операції не допускаються. Якщо функція оримала невірний тип данних для операції (не числа) або
# неприпустимий (невідомий) тип операції вона повинна повернути None і вивести повідомлення "Невірний тип даних" або
# "Операція не підтримується" відповідно.

def stupid_calc(num1, num2, operation):
    """
    Simple calculator for 4 math operations: + = / *
    :param num1: first number
    :type num1: int
    :param num2: second number
    :type num2: int
    :param operation: math operator for num1 and num2
    :type operation: str
    :return: result of operation with num1 and num2
    :rtype: int or float
    """
    if not isinstance(num1, int) and isinstance(num2, int):
        print("Wrong data type")
        return None

    if isinstance(num1, bool) or isinstance(num2, bool):
        print("Wrong data type")
        return None

    if not isinstance(operation, str):
        print("Wrong data type")
        return None

    if operation == "+":
        result = num1 + num2
        print(result)
    elif operation == "-":
        result = num1 + num2
        print(result)
    elif operation == "/":
        result = num1 / num2
        print(result)
    elif operation == "*":
        result = num1 * num2
        print(result)
    else:
        print("This operation is not possible here.")


stupid_calc(3, 4, "/")




# task 3. Напишіть докстрінг для обох функцій

