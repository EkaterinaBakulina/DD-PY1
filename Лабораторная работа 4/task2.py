DEFAULT_COUNT = 0


def dictionary_for_text(str_):
    transformation_str_1 = "".join(str_.split())
    transformation_str_2 = transformation_str_1.lower()
    transformation_str_3 = list(transformation_str_2)
    list_ = []
    for letter in transformation_str_3:
        if letter.isalpha() is True:
            list_.append(letter)
    dictionary = {}
    for key in list_:
        dictionary[key] = dictionary.get(key, DEFAULT_COUNT) + 1
    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(dictionary_for_text(main_str))
dict_ = (dictionary_for_text(main_str))


def new_dictionary_for_text(old_dictionary):
    new_dictionary = {}
    for symbol, amount_of_certain_letter in old_dictionary.items():
        amount_of_certain_letter_in_percent = round(amount_of_certain_letter * 100 / sum(old_dictionary.values()), 2)
        new_dictionary[symbol] = new_dictionary.get(symbol, amount_of_certain_letter_in_percent)
    return new_dictionary


print(new_dictionary_for_text(dict_))
