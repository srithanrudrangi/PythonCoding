numOfYears = int(input('How many years? '))

for i in range(numOfYears):
    totalInchesOfrainfall = 0
    currentMonth = 1
    for currentMonth in range(1, 13):
        inchesOfrainfall = int(
            input('How many inches of rainfall for the month of ' + format(currentMonth, "d") + ': '))
        totalInchesOfrainfall += inchesOfrainfall
    print('The total inches of rainfall is: ',
          totalInchesOfrainfall, ' inches')
    average = totalInchesOfrainfall/12
    print('The average amount of rainfall is: ', average, ' inches')
