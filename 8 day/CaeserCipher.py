import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']




def cipher(shift, text, direction):
    if direction == 'encode':
        alp = alphabet
        alp.extend(alphabet)
        for j in range(len(text)):
            index = alphabet.index(text[j])
            print(alp[index + shift], end='')

    elif direction == 'decode':
        alp_d = alphabet
        alp_d.extend(alphabet)
        position = 26
        for k in range(len(text)):
            index_d = alphabet.index(text[k]) - shift
            print(alp_d[26 + index_d], end='')
    else:
        print('error')
        rstrt = input('Restart the program? ').lower()
        if rstrt == 'yes' or rstrt == 'y':
            cipher()



while True:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    cipher(shift, text, direction)
    print()
    answer = input('End, try again? (y/n)').lower()
    if answer not in ('y', 'n'):
        break
        print('Invalid input')
    if answer == 'y':
        continue
    else:
        print('Bye')
        break
