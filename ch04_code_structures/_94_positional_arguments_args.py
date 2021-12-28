'''
author: oscar
date: 2021-12-27 19:07
'''

#imports



#functions
def print_args(*args):
    print('Positional argument tuple:', args)

if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'empty parameter')
    print('===============================================')
    
    #in a functions, an * groups a variable number of positional
    #arguments into a tuple of parameter values.
    print_args()
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'set up some parameters')
    print('===============================================')
    print_args(3, 2, 1, 'wait', 'uh...')


    