from pprint import pprint
list_ = []
for i in range(16):
    spisok = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    list_.append(spisok)
pprint(list_)
