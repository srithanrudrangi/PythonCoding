numOfSecondsGiven = int(input('Enter a number of seconds: '))

days = int(numOfSecondsGiven / 86400)
print('Days: ', days)

hours = int(((numOfSecondsGiven % 86400) % 3600)/60)
print('Hours: ', hours)


# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
