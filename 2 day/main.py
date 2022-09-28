
print('Tip calculator')

total = float(input('What is your total bill: $'))

split = float(input('How many people to split the bill: '))

percents = float(input('How many percents to give? (10, 12, 15): '))

pay = (total + ((total * percents)/100)) / split


print('Every person should pay: ' + str(round(pay, 1)))

