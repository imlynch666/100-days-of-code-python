import random


cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print('Welcome')
def choice():
    global result
    result = input('Do you want to play blackjack? Type "y" or "n"')
#
def blackjack(cards_list):
    print('\n' * 50)

    player_list = []
    player_list.extend(random.sample(cards_list, 2))
    for j in range(len(player_list)):
        if player_list[j] in cards_list:
            cards_list.remove(player_list[j])
    print(f'Your cards: {player_list}, current score is: {sum(player_list)}')

    comp_list = []
    comp_list.extend((random.sample(cards_list, 2)))
    print(f'Computer cards: {comp_list}, current score is: {sum(comp_list)}')

    choice_2 = input('Type "y" to get another card, type "n" to pass \n')

    if choice_2 == 'y':
        player_list.extend(random.sample(cards_list, 1))

    print(f'Your cards if {player_list}, current score is {sum(player_list)}')
    print(f'Computer card: {sum(comp_list)}')
    if sum(player_list) <= 21 and sum(player_list) > sum(comp_list):
        print('You WIN')
    elif sum(player_list) > 21:
        print('You went over, lose')
    else:
        print('DRAW')

choice()

if result == 'y':
    blackjack(cards_list)
else:
    print('bye')