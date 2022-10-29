def delete(list_, index=None):
        if index == None:
                extra_number = list_[-1]
                new_list_ = list_[:-1]    # по умолчанию лишний элемент - последний в списке
        else:
                extra_number = list_[index]
                new_list_ = list_[:index] + list_[index+1:]    # если индекс задан, то лишний элемент определяется по этому индексу
        return new_list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
