list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num = list_numbers[0]

for index, value in enumerate(list_numbers):
    if value >= max_num:
        max_num = value
        index_num = index

index_last_num = len(list_numbers) - 1

list_numbers[index_num], list_numbers[index_last_num] = list_numbers[index_last_num], list_numbers[index_num]

print(list_numbers)
