#2440
n = int(input())
for i in range(n):
  print("*" * (n-i))
  i += 1

#2441
n = int(input())
for i in range(n):
  print((" "*i) + ("*"*(n-i)))
  i += 1