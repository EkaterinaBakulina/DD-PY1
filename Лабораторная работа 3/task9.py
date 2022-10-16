salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for var in range(1, 11):
    var = spend - salary
    need_money += var
    spend += spend * increase

print(round(need_money))
