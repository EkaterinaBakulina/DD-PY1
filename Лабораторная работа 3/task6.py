list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_max_element = 0  # ищем индекс максимального элемента в списке
for i, current_var in enumerate(list_numbers):
    var = list_numbers[index_max_element]
    if current_var > var:
        index_max_element = i

list_numbers[index_max_element], list_numbers[-1] = list_numbers[-1], list_numbers[index_max_element]

print(list_numbers)
