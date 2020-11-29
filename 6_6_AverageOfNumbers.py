def main():
    infile = open('numbers.txt', 'r')
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    infile.close()
    average = num1 + num2 + num3/3
    print('The numbers are:', num1, num2, num3)
    print('Their average is:', average)


main()
