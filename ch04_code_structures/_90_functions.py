'''
author: mrgracias
Year: 2021
'''
# imports


# functions
def main():
    print(commentary('blue'))


def commentary(color):
    if color == 'red':
        return 'it is a tomato'
    elif color == 'green':
        return 'it is a green pepper'
    elif color == 'bee purple':
        return 'I don\'t know what is it, but bees can see it'
    else:
        return 'I\'ve never heard of this color'


def if_none(sym, thing):
    if thing is None:
        print(sym, 'It\'s None')
    elif thing:
        print(sym, 'It\'s true')
    else:
        print("It's false")
    
        
if __name__ == '__main__':
    main()
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' The importance of None')
    print('===============================================')
    if_none('None:', None)
    if_none('True:', True)
    if_none('False', False)
    if_none('0', 0)
    if_none('0.0', 0.0)
    if_none('()', ())
    if_none('[]', [])
    if_none('{}', {})
    
