#List,Set,Tuple

items = []
prices = []

while True: #无限循环:
   item = input("请输入想要购买的游戏: ")
   if item.lower() == "q":
       break
   price = float(input(f"请输入{item}的价格RM: "))
   items.append(item)
   prices.append(price)

print("游戏列表: ",items)
print("价钱列表： ",prices)

for index,item in enumerate(items): #enumerate (用这一行代码的方法可以列出list的索引及其物品)
    print("索引index:", index)
    print("Item:", item)

for Qty,item in enumerate(items):
    print(f"第{Qty+1}个商品是: {item},价格是RM {prices[Qty]:.2f}") #调用索引的时候用[],其他的不行，我试过了

total = sum(prices) #可以相加列表里面的数字

print(f"谢谢您，您的总消费是: RM{total:.2f}")