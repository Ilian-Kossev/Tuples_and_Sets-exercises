character_string = input()
occurrences_dict = {}
for el in character_string:
    if el not in occurrences_dict:
        occurrences_dict[el] = 0
    occurrences_dict[el] += 1
sorted_dict = dict(sorted(occurrences_dict.items()))
for key, value in sorted_dict.items():
    print(f'{key}: {value} time/s')

