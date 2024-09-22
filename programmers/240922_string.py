def change():
  #2744 of baekjoon
    s = input()
    for i in s:
        if i.isupper():
            print(i.lower(), end='')
        else:
            print(i.upper(), end='')

def cal():
  #2338 of baekjoon
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
