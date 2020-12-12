def main():
    txtFile = open('philosophers.txt', 'r')
    lineContent = txtFile.readline()
    noOfLines = 0

    while(lineContent != ""):
        noOfLines = noOfLines+1
        llineContentine = txtFile.readline()

    print('The number of line that are in philosophers.txt is: ', noOfLines)
    txtFile.close()

main()
