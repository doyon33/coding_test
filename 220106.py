#278
n = int(input())
# n >= 1 and n <= 100
for i in range(1, n+1) :
  print("*" * i)
  i += 1

#23972 -> unsolved
X = 0
i = 1
for i in range(i+K, 200000001):
  Y = (i - K) * N
  if i <= Y :
    X = i
    print(X)
    break
  else :
    i += 1
if X == 0 :
  print(-1)
inputValue = input()
L = inputValue.split()
K = int(L[0])
N = int(L[1])
Z = (N*K)/(N-1)
while X < Z:
  X += 1
print(X)

#2741
x = int(input())
for i in range(1, x+1):
  print(i)