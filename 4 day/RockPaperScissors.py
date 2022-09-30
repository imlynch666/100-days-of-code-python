import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('0 = Rock, 1 = Paper, 2 = Scissors')

list_of_choices = [rock, paper, scissors]

random_choice_value = random.choice(list_of_choices)
random_choice = list_of_choices.index(random_choice_value)
your_choice = int(input())

print(f'Your choice is: {list_of_choices[int(your_choice)]}')
print(f'Computer choice is: {random_choice_value}')

if your_choice == 0:
    if random_choice == 0:
        print('DRAW')
    elif random_choice == 1:
        print('LOSE')
    elif random_choice == 2:
        print('WIN')
elif your_choice == 1:
    if random_choice == 0:
        print('WIN')
    elif random_choice == 1:
        print('DRAW')
    elif random_choice == 2:
        print('LOSE')
elif your_choice == 2:
    if random_choice == 0:
        print('LOSE')
    elif random_choice == 1:
        print('WIN')
    elif random_choice == 2:
        print('DRAW')
else:
    print('ERROR')
