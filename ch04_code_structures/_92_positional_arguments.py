'''
author: mrgracias
Year: 2021
'''
# imports


# functions
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def menu1(wine, entree, dessert = 'pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def buggy(arg, result = []):
    result.append(arg)
    print(result)


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' positional arguments')
    print('===============================================')
    print(menu('chardonnay', 'chicken', 'cake'))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'Mix positional and keyword arguments')
    print('===============================================')
    # positional arguments come first
    print(menu('frontsenac', dessert='flan', entree='fish'))
    
    # look for menu1 function
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'Default values for parameters')
    print('===============================================')
    print(menu1('chardonnay', 'chicken'))
    print(menu1('zinfandel', 'duck', 'doughnut'))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' mutable data type like a list as parameter is an error')
    print('===============================================')
    buggy('a')
    buggy('b')
