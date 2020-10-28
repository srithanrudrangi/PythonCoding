numOfPackages = int(input('How many packages did you buy?'))
if ((numOfPackages >= 10) and (numOfPackages <= 19)):
    print('You get 10 percent discount.')
elif ((numOfPackages >= 20) and (numOfPackages <= 49)):
    print('You get 20 percent discount.')
elif ((numOfPackages >= 50) and (numOfPackages <= 99)):
    print('You get 30 percent discount.')
elif (numOfPackages > 99):
    print('You get 40 percent discount.')
else:
    print('You get 0 percent discount.')
