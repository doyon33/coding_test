n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    result = int(a)+int(b)
    print(f"Case #{i+1}: {result}")