# task 1. Напишіть функцію, яка приймає два аргументи.
# a. Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
# b. Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# c. В будь-якому іншому випадку - функція повертає кортеж з двох агрументів


def my_function(arg1, arg2):
    if isinstance(arg1, int) and isinstance(arg2, int):
        res = arg1 * arg2
    elif isinstance(arg1, float) and isinstance(arg2, float):
        res = arg1 * arg2
    elif isinstance(arg1, int) and isinstance(arg2, float):
        res = arg1 * arg2
    elif isinstance(arg1, float) and isinstance(arg2, int):
        res = arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        res = arg1 + arg2
    else:
        res = tuple
        res = (arg1, arg2)
    return res


user_constanta = my_function("paper", (1.5, "list", None))
print(user_constanta)


# task 2. Візьміть код з заняття і доопрацюйте натупним чином:
# a. користувач має вгадати чизло за певну кількість спроб. користувач на початку програми визначає кількість спроб
# b. додайте підказки. якщо рвзнися між числами більше 10 - "холодно", від 10 до 5 - "тепло", 1-4 - "гаряче"

# game
#
#     Number of attempts
#
#     Tips for user
#
#     AI -> number
#
#     User get number from keyboard
#
#     User == AI


from random import randint


def get_ai_number():
    number = randint(1, 10)
    print(f'AI: {number}')
    return number


def get_user_number(msg):
    while True:
        try:
            return int(input(f'{msg} (int): '))
        except ValueError:
            print('Number please!')


def check_numbers(ai_number, user_number):
    result = ai_number == user_number
    print(f'Result is: {result}')
    return result


def tips_for_users(ai_number, user_number):
    difference = abs(ai_number - user_number)
    if difference > 10:
        print("Cold!")
    elif 10 >= difference >= 5:
        print("Warm!")
    elif 5 > difference > 1:
        print("Hot!")


def game_guess_number():
    print('Game begins!')

    ai_number = get_ai_number()
    user_attempts = get_user_number('How many attempts do you want to try? ')
    attempts = 0

    while attempts < user_attempts:
        user_number = get_user_number('Enter the number. ')

        attempts += 1

        is_game_end = check_numbers(ai_number, user_number)

        if is_game_end:
            print('User win')
            return
        else:
            print('Wrong, try again!')

        if attempts >= user_attempts:
            print("You have no more attempts!")
            print('User loose!')
            return

        tips_for_users(ai_number, user_number)


game_guess_number()
