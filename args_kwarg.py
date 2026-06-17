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



