'''
@author: mrgracias
'''
#imports


#functions


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '1. using +=')
    print('===============================================')
    alphabet = ''
    alphabet += 'abcde'
    alphabet += 'fghijklmnopq'
    alphabet += 'rstuvwxyz'
    print(alphabet)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '2.using the \ character')
    print('===============================================')
    alphabet = ''
    alphabet = 'abcdefghi' + \
               'jklmnopqrst' + \
               'uvwxyz'
    print(alphabet)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '3.Use line continuation \ ')
    print('when computations span multiple lines')
    print('===============================================')
    print(1 + 2 + \
          3 + 4)
        
        