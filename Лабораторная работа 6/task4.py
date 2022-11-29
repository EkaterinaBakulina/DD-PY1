import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    list_of_data = []
    with open(filename) as f:
        for line_ in f:
            new_line = line_.replace(new_line, "")
            list_of_data.append(new_line.split(delimiter))
        columns = list_of_data[0]    #список заголовков
        index_where_names_of_columns = 0
        values = list_of_data[index_where_names_of_columns + 1:]    #список остальных значений (остальных списков значений)
        python_format = []
        for list_of_values in values:
            dict_ = {columns[i]: list_of_values[i] for i in range(len(columns))}
            python_format.append(dict_)
        return python_format



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
