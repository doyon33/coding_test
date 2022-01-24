# # #1284
def calculate(n):
  result = 0
  i = 0
  for i in range(len(n)):
    if n[i] == 0:
      result += 4
    elif n[i] == 1:
      result += 2
    else:
      result += 3
    i += 1
  space = len(n) + 2
  return (result + space)

print(calculate(str(5611)))

# l = []

# while True:
#   n = input()
#   if n == str(0):
#     break
#   else:
#     l.append(n)


# x = list(map(calculate,l))
# for j in x:
#   print(j)
