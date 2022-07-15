n = int(input())
elements_set = set()
for _ in range(n):
    for x in input().split():
        elements_set.add(x)
[print(x) for x in elements_set]