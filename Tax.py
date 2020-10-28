mealPrice = float(input('Enter the price of Meal:'))
tip = mealPrice*0.18
print('Your Tip is', tip)
salestax = mealPrice*0.07
print('Your Salestax is', salestax)
total = mealPrice+tip+salestax
print('Your Total is', total)
