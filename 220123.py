# # 1085
x, y, w, h = map(int, input().split())
valueList = [w-x, x, h-y, y]
MinDis = min(valueList)
print(MinDis)

#1267
def Y(n):
  x = n // 30
  y = x + 1
  return (y * 10)

def M(n):
  x = n // 60
  y = x + 1
  return (y * 15)

N = int(input())
history = input().split()
result_y = 0
result_m = 0

i = 0
for i in range(len(history)):
  result_y += Y(int(history[i]))
  i += 1

i = 0
for i in range(len(history)):
  result_m += M(int(history[i]))
  i += 1

if result_y > result_m :
  print("M", result_m)
elif result_y < result_m :
  print("Y", result_y)
else:
  print("Y", "M", result_y)