# Python 字典推导式

#dictionary =
#{key: expression for key,value in iterable}

# 运算

cities_in_f = {"LA":120,"New York":65,"Chicago":50,"miami":150}
cities_in_c = {key: round((value-32) *5/9,2) for key, value in cities_in_f.items()}

print(cities_in_f)
print(cities_in_c)

#ex2 条件判断

weather = {"Selangor": "Sunny", "KL": "Sunny", "Johor": "Rain", "Penang": "Rain"}

sunny_weather = {key:value for key, value in weather.items() if value == "Sunny"}
print(sunny_weather)

# ex3 条件判断 + 函式
cities_in_f = {"LA":120,"New York":65,"Chicago":50,"miami":150}
def check_temp(value):
    if value >= 70:
        return "Hot"
    elif value >= 40:
        return "Normal"
    else:
        return "Cold"
description_cities = {key: check_temp(value) for key, value in cities_in_f.items()}
print(description_cities)
