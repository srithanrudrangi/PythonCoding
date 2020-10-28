budget = int(input('What is your budget? '))
totalExpense = 0
moreExpense = 'y'

while (moreExpense == 'y'):
    price = int(input('Enter the price of your expense'))
    totalExpense = totalExpense + price
    moreExpense = input(
        'Do you have more Expense ? Type y for Yes or no for any other Key.')

print(totalExpense)
if totalExpense < budget:
    print('You spent under your budget.')
elif totalExpense > budget:
    print('You spent over your budget.')
else:
    print('You spent equal amount to your budget.')
