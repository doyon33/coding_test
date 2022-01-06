# task = int(input("how many tasks you have?"))
# task_list = []
# while i < task :
#   new_list = []
#   input_task = input()
#   new_list.append(input_task)

# n = input()
# print(n.split())

n = int(input())
if n >= 1 and n <= 9:
  for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')