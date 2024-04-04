from __init__ import *

def handelMultiLineInput(field = "the body"):
    numberOfLines = int(input(f"how many lines are you inputting for {field}: "))

    inputStorage = []

    for i in range(1, numberOfLines+1):
        inputStorage.append(input(f"body, line #{i}: "))


    return(inputStorage)


def message(snippet):
    print(f"your snippet is {snippet}")
    print(f"updating file...")
    sleep(.3)
    print(f"loading...")
    sleep(.3)
    print(f"loading...")
    sleep(.3)
    print(f"loading...")



def nameReplacement():
    return f"anonymous {7}"
