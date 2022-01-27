#1547
M = int(input())
i = 0
inputValue = []
for i in range(M):
  n = input().split()
  inputValue.append(n)
  i += 1

j = 0
P = str(1)
for j in range(M):
  X = inputValue[j][0]
  Y = inputValue[j][1]
  if P == X and P != Y:
    P = Y
  elif P!= X and P == Y:
    P = X
  elif P == X and P == Y:
    continue
  elif P != X and P != Y:
    continue
  else:
    print("-1")
    break
  j += 1

print(P)