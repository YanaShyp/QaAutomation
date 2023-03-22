# task 1 Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters",
# наприклад "Word 'Python' has 6 letters". Для отримання слова для аналізу скористайтеся константою або функцією input().

question = input("Type a word to know how many letters in it: ")
answer = "Word {} has {} letters.".format(question, len(question))
print(answer)

# task 2 Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік (можно використати
# константу або функцію input(), на екран має бути виведено лише одне повідомлення, також подумайте над варіантами,
# коли введені невірні дані).
# a. якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# b. якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# c. якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# d. якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
# e. у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"

str_data = input("Скільки вам років?")

if str_data.startswith("-"):
    print("Вік не може бути відʼємним")
elif str_data.isdigit():
    age = int(str_data)
    if age == 0 or age > 100:
        print("Введіть правильний вік")
    elif age < 7:
        print("Де твої батьки?")
    elif age >= 7 and age < 16:
        print("Це фільм для дорослих!")
    elif age > 65 and age <=100:
        print("Покажіть пенсійне посвідчення!")
    elif "7" in str(age):
        print("Вам сьогодні пощастить!")
    else:
        print("А білетів вже немає!")
else:
    print("Неправильно введені дані")

