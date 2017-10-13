
FLAG = [True]

def a():
    b()

def b():
    print(FLAG[0])
    FLAG[0] = False
    FLAG.append(True)
    print(FLAG[0])
    print(FLAG[1])

a()
