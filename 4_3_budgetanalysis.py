budget = int(input('What is your budget? '))
expenses = int(input('How many types of expeses are you buying?'))
totalExpense = 0

for i in range(expenses):
    price = int(input('Enter the price of your expense#'))
    totalExpense = totalExpense + price

print(totalExpense)
if totalExpense < budget:
    print('You spent under your budget.')
elif totalExpense > budget:
    print('You spent over your budget.')
else:
    print('You spent equal amount to your budget.')
