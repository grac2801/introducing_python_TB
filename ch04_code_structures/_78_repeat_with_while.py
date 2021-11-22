'''
@author: mrgracias
'''
#imports


#functions


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '1.anatomy of a while loop')
    print('===============================================')
    count = 1
    while count <= 5:
        print(count)
        count+=1
        
        
        
        
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '2.cancel with break')
    print('===============================================')
    while True:
        stuff = input('String to capitalize [type q for quit] ')
        if stuff == 'q' or stuff == 'Q':
            print('Program ended. Thanks.\n')
            break
        print(stuff.capitalize())
        
        
        
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '3.skip ahead with continue')
    print('===============================================')
    while True:
        value = input('Integer, please [q to end]: ')
        if value == 'q' or value == 'Q':
            break
        number = int(value)
        if number % 2 == 0:
            continue
        print(number, 'squared is:', number  ** 2)
        
        
        
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '4.check break use with else')
    print('===============================================')
    numbers = [1, 3, 5]
    position = 0
    while position < len(numbers):
        number = numbers[position]
        if number % 2 == 0:
            print('found even number: ' + number)
            break
        position += 1
    else: #break is not called if break occurs
        print('no even number found')
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        