from random import randint


def get_unique_list_numbers() -> list[int]:
    list_ = [randint(-10, 10) for _ in range(15)]
    while len(set(list_)) != 15:
        for number in list_:
            if list_.count(number) > 1:
                list_.remove(number)
                new_number = randint(-10, 10)
                while new_number in list_:
                    new_number = randint(-10, 10)
                list_.append(new_number)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
