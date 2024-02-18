#My Coffee Shop Simulator

#assigns a value to the variables coffee_price, muffin_price, cheese_danish_price, and donut_price
coffee_price = int(5)
muffin_price = int(4)
cheese_danish_price = int(6)
donut_price = int(4)

#asks the customer for their order
coffee_amount = int(input('How many coffees would you like to order?\n'))
muffin_amount = int(input('How many muffins can I get you?\n'))
cheese_danish_amount = int(input('How may cheese danishes would you like?\n'))
donut_amount = int(input('How many donuts can I interest you in today?\n'))

#assigns the sales tax amount to the variable sales_tax
sales_tax = float(.06)

#calculates the value of individual items ordered and creates the new variables
coffee_total = coffee_amount * coffee_price
muffin_total = muffin_amount * muffin_price
cheese_danish_total = cheese_danish_amount * cheese_danish_price
donut_total = donut_amount * donut_price

#calculates the subtotal and creates the subtotal variable
subtotal = coffee_total + muffin_total + cheese_danish_total + donut_total

#calculates the amount of tax and creates the tax variable
tax = sales_tax * subtotal

#calculates the total amount to be paid and creates the total variable
total = subtotal + tax

#displays the receipt and utilizes the variables made previously
print('\n*****************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought')
print(coffee_amount)
print('Number of muffins bought?')
print(muffin_amount)
print('Number of cheese danishes bought?')
print(cheese_danish_amount)
print('Number of donuts bought?')
print(donut_amount)
print('******************************************\n')
print('******************************************')
print('My Coffee and Muffin Shop Receipt')
print(coffee_amount, 'Coffee at $5 each: $', coffee_total)
print(muffin_amount, 'Muffins at $4 each: $', muffin_total)
print(cheese_danish_amount, 'Cheese Danishes at $6 each: $', cheese_danish_total)
print(donut_amount, 'Donuts at $4 each: $', donut_total)
print('6% tax: $', tax)
print('----------')
print('Total: $', total, '\n')
print('Thanks for stopping by, have a wonderful day!')
