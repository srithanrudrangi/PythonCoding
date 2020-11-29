def main():
    num_days = int(input('For how many days do you have sales? '))
    sales_file = open('sales.txt', 'w')
    for count in range(1, num_days + 1):
        sales = float(input('Enter the sales for day  #' + str(count) + ':'))
        sales_file.write('Enter the sales for day #  ' +
                         str(count) + ': '+str(sales) + '\n')
    sales_file.close()
    print('Data written to sales.txt.')


main()
