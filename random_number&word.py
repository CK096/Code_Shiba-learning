import random

#randint() #显示随机号码
print(random.randint(1,10))

#random() #显示随机浮点数
print(random.random())

#列表中随机一个元素
option = ["石头","剪刀","布"]
rand_option = random.choice(option)
print(rand_option)

#把一个列表打乱
card = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(card)
print(card)

#猜数字游戏
import random
low = 1
high = 100
answer = random.randint(low, high)
guesses = 0

while True:
    guess = int(input(f"Guess a number between {low} and {high}: "))
    guesses += 1
    if guess < answer:
        print("this number is smaller than the answer")
    elif guess > answer:
        print("this number is higher than the answer")
    else :
        print(f"Congratulation, {answer}  is the correct number, your re total guess {guesses} times")
        break