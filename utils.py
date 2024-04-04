from __init__ import *

def handelMultiLineInput(field = "the body"):
    """if the user wishes to enter 1 line then they just answer with one and the program works as expected"""
    numberOfLines = int(input(f"how many lines are you inputting for {field}: "))

    inputStorage = []

    for i in range(1, numberOfLines+1):
        inputStorage.append(input(f"body, line #{i}: "))


    return(inputStorage)


def message(snippet):
    """a little bit of fake loading for effect"""
    print(f"your snippet is {snippet}")
    print(f"updating file...")
    sleep(.3)
    print(f"loading...")
    sleep(.3)
    print(f"loading...")
    sleep(.3)
    print(f"loading...")



def autoName():
    """if no name is provided then its automatically assigned a name (anonymous x)"""
    with open("text.txt", "a") as textFile:
        textFile.write(str(len(open("text.txt").readlines())+1))
    with open("text.txt", "r") as textFile:
        la: int = textFile.readline()
    return f"anonymous {la}"
