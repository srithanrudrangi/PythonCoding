date = int(input('Enter a Month in numeric form:'))
magic = int(input('Enter a Day in numeric form:'))
bat = int(input('Enter a Two digit Year in numeric form:'))
fan = (date*magic)
if fan == bat:
    print('Your date is a magic date.')
else:
    print('Your date is not a magic date.')
