n = int(input())
odd_nums_set = set()
even_nums_set = set()
row = 0
for _ in range(n):
    row += 1
    names = input()
    sum_ascii_values = 0
    for el in names:
        sum_ascii_values += ord(el)
    result = int(sum_ascii_values / row)
    if result % 2 == 0:
        even_nums_set.add(result)
    else:
        odd_nums_set.add(result)
sum_odd_set_nums = sum(odd_nums_set)
sum_even_set_nums = sum(even_nums_set)
if sum_even_set_nums == sum_odd_set_nums:
    res = [str(x) for x in odd_nums_set | even_nums_set]
    print(', '.join(res))
if sum_odd_set_nums > sum_even_set_nums:
    res = [str(x) for x in odd_nums_set - even_nums_set]
    print(', '.join(res))
else:
    res = [str(x) for x in even_nums_set ^ odd_nums_set]
    print(', '.join(res))
