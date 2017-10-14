# This is just a dummy-function instead of using print with text, 
# wich will not be needed anymore when app is further developed.
def dummy(*text):
    print(*text)

# This is just a dummy-function instead of using input with text, 
# wich will not be needed anymore when app is further developed.
def stick(*text):
    hit = input(*text)
    return hit


from time import sleep

sleepFlag = False

def sleepif(seconds):
    if sleepFlag == True:
        sleep(seconds)
