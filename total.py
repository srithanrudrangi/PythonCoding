
print("What is price of item 1 ?")
item1 = float(input())

item2 = float(input("What is price of item 2 ?"))

subTotal = item1 + item2

print('Your Sub total: $', subTotal)
Tax = subTotal*0.07
print('Your Sales Tax: $', Tax)
Total = subTotal+Tax
print('Total you pay: $', Total)
