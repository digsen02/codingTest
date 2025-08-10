N = int(input())

a = list(map(int, input().split()))
print(sum(a) / max(a) * 100 / N)