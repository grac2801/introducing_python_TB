'''
author: oscar
date: 2021-12-31 13:06
'''

#imports


#functions
def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)

if __name__ == '__main__':
    #===========================================================================
    # if *args and **kwargs are used, they need to be used in that order.
    #===========================================================================
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'call on the **kwargs function')
    print('===============================================')
    print_kwargs(drink = 'soda', entree = 'steak',  dessert = 'chocolate cake')