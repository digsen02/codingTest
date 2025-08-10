s = input()
result = list()

for i in range(97, 123):
    ishave = False
    for _s in s:
        if _s == chr(i):
            result.append(s.find(chr(i)))
            ishave = True
            break
    if not ishave :
        result.append(-1)
print(*result)