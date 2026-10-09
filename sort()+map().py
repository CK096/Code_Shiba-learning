# Python sort()

#list
number_list = [1,3,5,2,4]
print(number_list)
number_list.sort()
print(number_list)
number_list.sort(reverse=True)
print(number_list)

str_list = ["Jack","Lin","Tom","Andy"]
print(str_list)
str_list.sort()
print(str_list)
str_list.sort(reverse=True)
print(str_list)

#元组的排列 Tuple
students = [("Lin",170,"C"),("Tan",168,"B"),("Lee",176,"A")]
sorted_student = sorted(students,key=lambda x: x[1])
print(students)

================================================================

# Python 中的 map

# map(可迭代的[列表]，函式)

store = [("pant",20),("shirt",30),("Jacket",50),("sock",10)]

to_myr= lambda date: (date[0],date[1] *4.05)
store_myr = list(map(to_myr, store))
print(store_myr)

to_usd = list(map(lambda date: (date[0],date[1] /4.05),store))
print(to_usd)

==============================================================
# Python中的filter()

friends = [("Bob",18),("lin",17),("lee",19),("Tam",16)]

adult = list(filter(lambda age: age[1] >= 18, friends))
for friend in adult:
    print(f"{friend[0]} is adult")
