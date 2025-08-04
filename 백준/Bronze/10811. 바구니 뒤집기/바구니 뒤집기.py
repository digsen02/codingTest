N, M = map(int, input().split())

integers = list(range(1, N + 1))

for _ in range(1, M + 1):
    i, j = map(int, input().split())
    integers[i-1:j] = integers[i-1:j][::-1]
print(*integers)
