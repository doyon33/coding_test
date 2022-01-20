# #2439
n = int(input())
z = " "
i = 1
while i in range(n+1) :
  space = str(z * (n - i))
  star = "*" * i
  print(space + star)
  i += 1

#2742
n = int(input())
i = 0
for i in range(n):
    print(n - i)
    i += 1