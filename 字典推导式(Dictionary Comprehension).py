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

# ex4 加入内建函式
scores = {"alice": 85,"bob": 55,"charlie": 92,"david": 48}

result = {key.upper():value + 5 for key,value in scores.items() if value >= 60}
print(result)

# ex5 倒反 key, value
countries = {"Malaysia": "Kuala Lumpur","Japan": "Tokyo","Thailand": "Bangkok","Singapore": "Singapore"}

result = {value:key for key,value in countries.items()}
print(result)

# ex6 更改 key/Value
temperatures = {"Kuala Lumpur": 32,"Tokyo": 18,"Seoul": 12,"Bangkok": 35,"London": 8}

result = {key : "Hot" if value >=20 else "Cold" for key,value in temperatures.items()}
print(result)

prices = {"Apple": 100,"Banana": 50,"Orange": 80,"Mango": 150}

result = {key.upper() : round(value * 0.9 if value >= 100 else value * 1.1,2) for key,value in prices.items()}
print(result)
