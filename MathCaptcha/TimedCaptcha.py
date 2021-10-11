import random
import string
import sys
from threading import Timer


def text_captcha():
    """
    It generates a captcha and asks user to verify within 9 seconds.
    """

    captcha = string.ascii_lowercase + string.ascii_uppercase + \
              "".join([str(i) for i in range(0, 10)])
    captcha_random = ''
    while len(captcha_random) < 10:
        char = random.choice(captcha)
        captcha_random += char

    time = Timer(9, timeout)
    print("Captcha: " + captcha_random)
    time.start()
    user_input = input("Enter the characters in Captcha: ")
    verify(user_input, captcha_random, time)
    time.cancel()


def timeout():
    """
    It tells users that time has run out and provides users options.

    :return: presents users options to either quit or try again after timeout.
    """

    print("Timeout. \nPlease type 'quit' to quit or 'try' to try again.")


def verify(input: str, captcha: str, time: Timer):
    """
    A helper function for text_captcha. It checks if the user input matches the
    given captcha and executes according to the options presented after timeout.

    :param time: timer object from text_captcha
    :param input: the input of the user
    :param captcha: the random captcha that was created in text_captcha
    """

    if input == captcha and time.is_alive():
        print("Verified as human!")
    elif input == "quit":
        sys.exit("The program has ended.")
    elif input == "try":
        text_captcha()
    elif input != captcha:
        print("Prove you're a human because your previous "
              "input didn't match Captcha.")
        text_captcha()


if __name__ == '__main__':
    text_captcha()
