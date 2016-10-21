import re


def get_password_strength(password):
    digits = re.findall(r'\d',password)
    if len(digits) == len(password): #пароль состоит только из чисел?
        return 1
    letters = re.findall(r'\w\D',password)
    upper_letters = 0
    for letter in letters:
        if letter.isupper():
            upper_letters += 1
    if len(letters) == len(password):#пароль состоит только из букв?
        return 1 if upper_letters == 0 else 2
    strength = 2
    lower_letters = len(letters) - upper_letters
    strength += oneormoretimes(upper_letters)
    strength += oneormoretimes(lower_letters)
    strength += oneormoretimes(len(digits))
    symbols = re.findall(r'\W',password)
    strength += oneormoretimes(len(symbols))
    return strength


def oneormoretimes(digit):
    return 1 if digit == 1 else (2 if digit > 1 else 0)


if __name__ == '__main__':
    print (get_password_strength("123a"))
