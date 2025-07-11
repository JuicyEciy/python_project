#Tip Calculator
name = input('What is your name? ')
cost = float(input('What is the cost of your meal? '))
tip = int(input('What percentage tip would you like to give? '))
split = int(input('How many of you to split the bill? '))

your_tip = tip / 100 * cost
total_bill = cost + your_tip
split_bill = total_bill / split

print(f'\nWelcome, {name}!')
print(f'You should leave a tip of: ${your_tip:.2f}')
print(f'Total bill is: ${total_bill:.2f}')
print(f'Each one of you should pay: ${split_bill:.2f}')
