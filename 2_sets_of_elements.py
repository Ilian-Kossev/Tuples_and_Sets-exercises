length_set_1, length_set_2 = input().split()
set_1 = {input() for _ in range(int(length_set_1))}
set_2 = {input() for _ in range(int(length_set_2))}
set_3 = set_1 & set_2
[print(x) for x in set_3]