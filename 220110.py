import sys
T = int(sys.stdin.readline().rstrip())
i = 0
tasks = [None] * T
while i in range(T):
  x = sys.stdin.readline().rstrip()
  tasks[i] = x
  i += 1
j = 0
while j in range(T):
  z = tasks[j].split()[0] ** tasks[j].split()[1]
  result = tasks[j] % 10
  print(result)
  j += 1
