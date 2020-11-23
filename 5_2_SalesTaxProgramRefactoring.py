def sales():
    number = int(input(" How many items did you purchase? "))

    subTotal = 0

    for i in range(number):
        price = int(input("Enter price of item: "))
        subTotal = price + subTotal

    stateSalesTax = subTotal*0.05
    countySalesTax = subTotal*0.025

    print("Your Sub total:", subTotal)
    print("Your State sales Tax:", stateSalesTax)
    print("Your County sales Tax:", countySalesTax)
    print("Your Total due:", subTotal + stateSalesTax + countySalesTax)


sales()
sales()
