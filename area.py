length = int(input('What is the length of the first rectangle? '))
width = int(input('What is the width of the first rectangle? '))
num = length*width
print('The area of the first rectangle is: ', num)
first = int(input('what is the length of the second rectangle? '))
second = int(input('what is the width of the second rectangle? '))
area = first*second
print('The area of the second rectangle is: ', area)
if num == area:
    print('The area of both rectangles are Equal.')
elif num < area:
    print('The second rectangle has a greater area.')
else:
    print('The first rectangle has greater area')
