n = int(input())
longest_intersection = {}
current_intersection = {}
for _ in range(n):
    first_range, second_range = input().split('-')
    start_first_range = int(first_range.split(',')[0])
    end_first_range = int(first_range.split(',')[1])
    start_second_range = int(second_range.split(',')[0])
    end_second_range = int(second_range.split(',')[1])
    first_line = set()
    second_line = set()
    for num in range(start_first_range, end_first_range + 1):
        first_line.add(num)
    for num in range(start_second_range, end_second_range + 1):
        second_line.add(num)
    current_intersection = first_line & second_line
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
print(f'Longest intersection is {[x for x in longest_intersection]} with length {len(longest_intersection)}')
