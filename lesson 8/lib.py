import re

from functools import wraps

import time


def execution_time(func):
    @wraps(func)
    def execution_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} took {total_time:.4f} seconds')
        return result
    return execution_time_wrapper


@execution_time
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


@execution_time
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



