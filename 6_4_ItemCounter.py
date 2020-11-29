def main():
    txtFile = open('philosophers.txt', 'r')
    line = txtFile.readline()
    noOfLines = 0

    while(line != ""):
        noOfLines = noOfLines+1
        line = txtFile.readline()

    print('The number of line that are in philosophers.txt is: ', noOfLines)
    txtFile.close()


main()
