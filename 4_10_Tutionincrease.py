currentFee = 8000
print("YEAR", "\t", "FEE")
print("-----", "\t", "-----")

for i in range(1, 6):
    currentFee = currentFee + currentFee*(3/100)
    print(i, "\t$", currentFee)
