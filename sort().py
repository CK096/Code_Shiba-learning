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
