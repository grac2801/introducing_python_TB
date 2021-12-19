'''
@author: mrgracias
'''
#imports


#functions

#testing a push to GitHub
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
    
    #[first number is an expression]
    number_list = [number -1 for number in range(1, 6)]
    print('number list (number - 1): ', number_list)
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'adding a condition')
    print('===============================================')
    a_list = [number for number in range(1, 6) if number % 2 == 1]
    print(a_list)
    
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'compare to regular form')
    print('===============================================')
    a_list = []
    for number in range(1, 6):
        if number % 2 == 1:
            a_list.append(number)
    print(a_list)
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'Nested loops')
    print('===============================================')
    rows = range(1, 4)
    cols = range(1, 3)
    for row in rows:
        for col in cols:
            print(row, col)
            
            
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'multiplication table')
    print('===============================================')
    x = 5
    space = "{:<3}".format('')
    print(space, end = '')
    for row in range(1, 6):
        print(f'{x:<3}', end = '')
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    