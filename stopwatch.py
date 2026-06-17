import time #(import time 是时间模组)

#time.sleep(2) # .sleep() 这个是延时的时间,输入多少时间就会延时多少

my_time = int(input("请输入需要的秒数: "))

for x in reversed(range(my_time)):
    print(x)
    time.sleep(0)
print("Happy new Year")

for x in range(my_time, 0,-1): # 这样也可以倒数 (值, 0,-1)
    second = x % 60
    minits = x // 60
    print(f"{minits:02}:{second:02}")
    time.sleep(0)
print("Happy new Year")