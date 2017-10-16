from msvcrt import putwch
from msvcrt import getch
from msvcrt import getwch
from time import sleep
#import msvcrt # If successful, we are on Windows

while True:
    # Example of a prompt for one character of input
    promptStr   = "Please give me a character:"
    responseStr = "Thank you for giving me a {}."
    print(promptStr, end="\n> ")
    putwch(' ')
    answer = getch()
    print("\n")
    print(responseStr.format(answer))


