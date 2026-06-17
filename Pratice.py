Bank = []
Amount = []

while True:
    B = input("Please Key Bank Name: ")
    if B == "Stop":
           break
    A = float(input("Please Key Amount: RM "))
    Bank.append(B)
    Amount.append(A)
    Total = sum(Amount)

for E,F in enumerate(Bank):
    print(f'Your Saving Account {E+1} is {F}, Now have {Amount[E]}')

print("Total Your Money Have RM",Total)