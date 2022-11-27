import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    list_of_data = []
    with open(filename) as f:
        list_of_data.append(lines.split(delimiter) for lines in f)
        columns = list_of_data[0]    #список заголовков
        index_where_names_of_columns = 0
        values = list_of_data[index_where_names_of_columns + 1:]    #список остальных значений (остальных списков значений)
        for lists_of_values in values:
            python_format = [{columns[i]: lists_of_values[i]} for i in range(len(columns))]
    return python_format



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
