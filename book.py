numOfBooks = int(input('How books did you purchase?'))
if numOfBooks == 0:
    print('You recieved 0 points.')
elif numOfBooks == 2:
    print('You recieved 5 points.')
elif numOfBooks == 4:
    print('You have recieved 15 points.')
elif numOfBooks == 6:
    print('You recieved 30 points.')
elif numOfBooks >= 8:
    print('You recieved 60 points.')
else:
    print('You have 0 points')
