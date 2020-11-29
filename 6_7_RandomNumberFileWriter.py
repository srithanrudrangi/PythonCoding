import random


def main():
    randomnums = random.randint(1, 501)
    print('The file can hold 500 numbers.')
    file = open('randomnums.txt', 'a')
    file.write(str(randomnums) + '\n')
    file.close()
    print('Data written to randomnums.txt.')


main()
