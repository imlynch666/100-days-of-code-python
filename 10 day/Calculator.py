

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

dict_choice = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide

}


first_number = int(input('first number: '))
second_number = int(input('second number: '))



for key in dict_choice:
    print(key)
operators = input('choose the operator')

operator_choice = dict_choice[operators]
res = operator_choice(first_number, second_number)

print(f'{first_number} {operators} {second_number} = {res}')


while True:
    result = input(f'Type "y" if u want to continue operate with {res}, or type "n" t exit')
    if result == 'y':
        operators = input('choose the operator')
        third_number = int(input('number: '))
        operator_choice_2 = dict_choice[operators]
        res2 = operator_choice_2(res, third_number)
        print(f'{res} {operators} {third_number} = {res2}')
    if result == 'n':
        break


