import string
import random
str_1 = list(string.ascii_uppercase)
str_2 = list(string.ascii_lowercase)
str_3 = list(string.digits)
list_ = str_1 + str_2 + str_3
password_ = random.sample(list_, 8)
password = "".join(password_)
print(password)
