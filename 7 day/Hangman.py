import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

random_word = random.choice(word_list)

print(random_word)

###

chances = 5


for j in range(len(random_word)):
    print('_', sep='', end=' ')

print()
random_word_list = list(random_word)
random_word_under = []
for l in range(len(random_word_list)):
    random_word_under.append('_')
print(random_word_under)

while chances > 0:

    if chances == 4:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''')
    elif chances == 3:
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif chances == 2:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
    elif chances == 1:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''')
    print(f'You have {chances} chances.')
    letter = input('Print the letter: ')

    if letter in random_word:
        for k in range(len(random_word_list)):
            if random_word_list[k] == letter:
                random_word_under[k] = letter
                print(random_word_under[k], sep='', end='')
            else:
                print(random_word_under[k], sep='', end='')
    else:
        chances -= 1
if chances == 0:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''')
    print('You lose')