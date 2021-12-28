'''
author: oscar
date: 2021-12-27 19:06
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

def buggy1(arg):
    result = []
    result.append(arg)
    return result

def buggy3(args, result = None):
    if result is None:
        result = []
    result.append(args)
    return result

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
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'change function from buggy to buggy1')
    print('===============================================')
    print(buggy1('a'))
    print(buggy1('b'))

    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'Same buggy2 but using None')
    print('===============================================')
    print(buggy3('a'))
    print(buggy3('b'))