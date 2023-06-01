"""
Function Capital accepts and returns string that cleared of everything except uppercase letters.
In addition, the length of the string should not exceed 25 characters (anything more is simply cut off)
"""
def capital(string: str):
    if not isinstance(string,str):
        print("Wrong format. Enter string")
        return

    only_uppercase_string = ''.join(character for character in string if character.isupper())
    if len(only_uppercase_string) > 25:
        only_uppercase_string = only_uppercase_string[:25]
    print(only_uppercase_string)
    return only_uppercase_string

capital("Hi")
