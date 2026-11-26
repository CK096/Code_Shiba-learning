# args (arguments) 任意数量的参数 # * => tuple
def number(*lol):
    total = 0
    for x in lol:
        print (f"args: {x}")
        total += x
    return total
print(number(1,2,3,4))

# kwargs (关键字 + args) keyword args # ** => dictionary
def print_info(**info):
    for key, value in info.items():
        print(f'key: {key}, Value: {value}')
print_info(name="CK",age="25",Job="unknow")

# args 和 kwargs 一起用
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, 30, name="Alex", age=20)

#Big Example
def student_info(name,*score,**details):
    print(f"Student: {name}")
    print(f"Scores: {score}")
    total = sum(score)
    average = total / len(score)
    print(f"average: {average}")
    print(f"Details: {details}")

student_info("Alex",80, 90, 85,age=20,country="Malaysia")
