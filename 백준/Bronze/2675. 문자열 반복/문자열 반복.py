N = int(input())

for _ in range(N):
    R, S = map(str, input().split())
    P = ""
    for _S in S:
        for i in range(int(R)) :
            P += _S
    print(P)