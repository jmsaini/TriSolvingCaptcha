import random
import string


def equation_captcha() -> str:
    """
    It generates a math equation that has operators (such as addition,
    subtraction, multiplication, exponent, and/or division) and operands.
    :return: a random captcha with operators and operands
    """
    operators = ["+", "-", "*", "÷", "^"]

    random_captcha = ""

    while len(random_captcha) < 8:
        num1 = random.randint(0, 9)
        operator = random.choice(operators)
        num2 = random.randint(0, 9)
        if operator == "÷":
            if num2 == 0:
                continue
            elif num1 % num2 != 0:
                num1 = random.choice(list(range(2, 9, 2)))
                num2 = 2
        if operator == "^" and (num1 ** num2) > 20:
            continue
        random_captcha += "(" + str(num1) + operator + str(num2) + ")"

    return random_captcha + " = " + " __"


def verify_input(user_input: str, captcha: str) -> bool:
    """
    A helper function for equation_captcha.
    It checks if the user input matches the given captcha.

    :param user_input: the input of the user
    :param captcha: the random captcha that was created in equation_captcha
    :return: true if the input matches the captcha or false if it doesn't match
    """
    compare = ""
    for i in range(1, len(captcha) - 6):
        # finding the mid and replacing with a multiplication sign
        if captcha[i] == ")" and captcha[i + 1] == "(":
            compare += "*"
        elif captcha[i] == "÷":
            compare += '/'
        elif captcha[i] == "^":
            compare += "**"
        elif captcha[i] != "(" or captcha[i] != ")":
            compare += captcha[i]

    # print(compare)

    if user_input == eval(compare):
        return True
    else:
        return False
