'''
author: mrgracias
Year: 2021
'''
# imports


# functions
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' positional arguments')
    print('===============================================')
    print(menu('chardonnay', 'chicken', 'cake'))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' positional and keyword arguments')
    print('===============================================')
    print(menu('frontsenac', dessert='flan', entree='fish'))
