'''
@author: mrgracias
'''
#imports


#functions


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'Not comprehension way')
    print('===============================================')
    number_list = []
    number_list.append(1)
    number_list.append(2)
    number_list.append(3)
    print(number_list)
    
    print()
    number_list = []
    for number in range(1, 4):
        number_list.append(number)
    print(number_list)
    
    
    print()
    print(list(range(1, 4)))
    
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'comprehensions')
    print('===============================================')
    #[Expression for item in iterable]
    number_list = [number for number in range(1, 6)]
    print(number_list)
        