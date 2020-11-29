# This program writes three lines of data
def main():
    file = open('numbers.txt', 'w')
    file.write('One\n')
    file.write('Two\n')
    file.write('Three\n')
    file.close()


main()
