# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_days = 90 * 365

total_weeks = 90 * (52)

total_month = 90 * 12


days = total_days - (int(age) * 365)
weeks = total_weeks - (int(age) * (52))
month = total_month - (int(age) * 12)


print(f'You have {days} days, {weeks} weeks, {month} month left')






