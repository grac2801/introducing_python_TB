'''
@author: mrgracias
'''
#imports


#functions


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '1.while loop')
    print('===============================================')
    rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
    current = 0
    while(current < len(rabbits)):
        print(rabbits[current])
        current += 1
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '2.Quick for loop')
    print('===============================================')
    for i in rabbits:
        print(i)
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '3.iterable strings')
    print('===============================================')
    word = 'cat'
    for letter in word:
        print(letter)
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '4.iterate over a dictionary')
    print('===============================================')
    accusation = {'room': 'ballroom', 
                  'weapon': 'lead pipe', \
                  'person':'Col. Mustard'}
    for card in accusation: #all keys() will be selected
        print(card)
        
    print('\n\n')   
    for val in accusation.values():
        print(val)
        
    print('\n\n')   
    for item in accusation.items():#all items
        print(item)
        
    print('\n\n')#you can assign to a tuple
    for card, contents in accusation.items():
        print('Card', card, ' has the contents:', contents)  
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '5.break use with else')
    print('===============================================')
    cheeses = ['']
    for cheese in cheeses:
        print('this shop has some lovely', cheese)
        break
    else:
        print('this is not much of a cheese shop')
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '6.break use with else')
    print('===============================================')
    cheeses = []
    found_one = False
    for cheese in cheeses:
        found_one = True
        print('this shop has some lovely',cheese)
        break
    if not found_one:
        print('this is not much of a cheese shop')
     
             
    
    
    
    
    
    
    
    
    