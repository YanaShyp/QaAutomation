# task 1. Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" (враховуються як великі
# так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".

while True:
    user_input = input("Введіть слово, яке містить букву 'о': ")

    if user_input.count("О") or user_input.count("о") > 0:
        print("Дякую!")
        break

    if user_input.count("О") or user_input.count("о") == 0:
         print("Тут немає букви 'о'.")
         continue


# task 2. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть
# код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Зауважте,
# що lst1 не є статичним і може формуватися динамічно від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for element in lst1:
    if isinstance(element, str):
        lst2.append(element)

print(lst2)


# task 3. Є стрінг з певним текстом (можна скористатися input або константою). Напишіть код, який визначить кількість
# слів в цьому тексті, які закінчуються на "о" (враховуються як великі так і маленькі).


user_input = input("Введіть речення: ")

answer_list = user_input.split()
non_capital = "о"
capital = "О"
res = 0
for element in answer_list:
    if isinstance(element, str):
        strip_element = element.strip(".,?:!")
        if strip_element.endswith(capital) or strip_element.endswith(non_capital):
            res += 1
        else:
            res == 0
    else:
        print("Невірні дані")

print(res)

