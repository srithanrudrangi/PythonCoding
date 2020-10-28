numOfCoins = int(input('How many coins do you need to make one dollar ?'))
penny = int(input('Enter some amount of pennies to make part of 1 dollar?'))
nickel = int(input('Enter some amount of nickel to make part of 1 dollar?'))
dimes = int(input('Enter some amount of dimes to make part of 1 dollars?'))
quarters = int(input(
    'Enter some amount of quarters to make a full dollar including pennies, nickels, and dimes.'))
if penny + nickel + dimes + quarters == 100:
    print('Congratulations your coins Equals 1 dollar.')
