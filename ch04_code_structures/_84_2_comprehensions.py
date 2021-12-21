'''
@author: mrgracias
'''
# imports

# functions

# testing a push to GitHub
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
    # [Expression for item in iterable]
    number_list = [number for number in range(1, 6)]
    print(number_list)
    
    # [first number is an expression]
    number_list = [number - 1 for number in range(1, 6)]
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
    print('TOPIC: --->', "Now let's use a comprehension")
    print('===============================================')
    rows = range(1, 4)
    cols = range(1, 3)
    cells = [(row, col) for row in rows for col in cols]
    for cell in cells:
        print(cell)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' tuple unpacking')
    print('===============================================')
    rows = range(1, 4)
    cols = range(1, 3)
    cells = [(row, col) for row in rows for col in cols]
    for a, b in cells:
        print(a, b)
    
    #===========================================================================
    # Have students do this part as an exercise
    #===========================================================================
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'multiplication table')
    print('===============================================')
    print(f'{"":<5}', end='')
    for row in range(1, 6):
            print(f'{row:<5}', end='')
    print()
    for leftCols in range(1, 6):
        print(f'{leftCols:<5}', end='')
        for row in range(1, 6):
            print(f'{leftCols * row:<5}', end='')
        print()

    
