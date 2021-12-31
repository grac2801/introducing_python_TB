'''
author: oscar
date: 2021-12-31 13:18
'''

#imports


#functions
def echo(anything):
    'echo returns its input argument'
    print(anything)

if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'call function with docstring')
    print('===============================================')
    echo('Hello')
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'call the docstring')
    print('===============================================')
    
    print(echo.__doc__)
    help(echo)