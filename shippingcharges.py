numOfPounds = int(input('How many pounds will you carry?'))
if (numOfPounds <= 2):
    print('You get $1.50')
elif ((numOfPounds > 2) and (numOfPounds < 7)):
    print('You get $3.00')
elif ((numOfPounds > 6) and (numOfPounds < 11)):
    print('You get $4.00')
else:
    print('You get $4.75')
