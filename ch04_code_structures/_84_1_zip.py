'''
@author: mrgracias
'''
#imports


#functions


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'The use of zip')
    print('===============================================')
    days = ['monday', 'tuesday', 'wednesday']
    fruits = ['banana', 'orange', 'peach']
    drinks = ['coffee', 'tea', 'beer']
    desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
    for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
        print(day, ': drink', drink, '- eat', fruit, '- enjoy', dessert)
        
    print()
    english = ('Monday', 'Tuesday', 'Wednesday')
    french = 'Lundi', 'Mardi', 'Mercredi'
    print(list(zip(english, french)))
    
    print()
    print(dict(zip(english, french)))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'range()')
    print('===============================================')
    for x in range(0,3):
        print(x)
    
    print()
    print(list(range(5))) 
    
    print()
    for x in range(2, -1, -1):
        print(x)  
        
     
    
        