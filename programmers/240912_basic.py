def numb1271():
    inputtxt = input()

    arr = inputtxt.split(" ")
    money = arr[0]
    life = arr[1]

    money = int(money)
    life = int(life)
    print(money//life)
    print(money%life)

def numb1330():
    inputtxt = input()
    arr = inputtxt.split(" ")
    a = int(arr[0])
    b = int(arr[1])

    if (a > b):
        print(">")
        return 0
    elif (a < b):
        print("<")
        return 0
    else:
        print("==")
        return 0

def numb31611():
    days = int(input())
    if (days%7 == 2):
        print(1)
        return 0
    else:
        print(0)
        return 0

def numb31610():
    a = int(input())
    b = int(input())
    c = int(input())

    total = a*b+c
    print(total)
    return 0
