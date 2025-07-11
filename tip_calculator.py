#Tip Calculator
name = input('what is your name? ')
cost = int(input('What is the cost of your meal? '))
tip = int(input('What percentage tip would you like to give? '))
split = int(input('How many of you to split the bill? '))

your_tip = float(tip / 100 * cost)
total_bill = float(your_tip + cost)
split_bill = float(cost / split)

print(f'Welcome, {name}')
print(f'You should leave a tip of: ${your_tip}')
print(f'total bill is: ${total_bill}')
print(f'Each one of you should pay: ${split_bill}')