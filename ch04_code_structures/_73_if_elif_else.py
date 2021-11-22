'''
@author: mrgracias
'''
#imports


#functions


if __name__ == '__main__':  
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '1.if')
    print('===============================================')
    disaster = True
    if(disaster):
        print('Woe')
    else:
        print('Yeah!')
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '2.if-else')
    print('===============================================')
    furry = False;
    small = True
    if furry:
        if small:
            print('it\'s a cat')
        else:
            print('It\'s a bear')
    else:
        if small:
            print('It\'s a skink')
        else:
            print('It\'s a hairless human')
            
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '3.elif')
    print('===============================================')
    color = 'tamarind'
    if color == 'red':
        print('it is a tomato')
    elif color == 'green':
        print('it is a green pepper')
    elif color == 'bee purple':
        print('I do not know what it is, but bees!')
    else:
        print('I\'ve never heard of the color', color)
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '4.relational operator list')
    print('===============================================')
    print('==', ': equal to')
    print('!=', ': not equal to')
    print('<', ': less than')
    print('<=', ': less than or equal to')
    print('>', ': greater than')
    print('>=', ': greater or equal to')
    print('in ..', ': membership')
    
    
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '5.these return boolean values')
    print('===============================================')
    x = 7;
    
    print('x == 5: ', x == 5)
    print('x == 7: ', x == 7)
    print('5 < x: ', 5 < x)
    print('x < 10: ', x < 10)
    
    print('to avoid conflict of precedence, use parenthesis')
    result = (5 < x) and (x < 10)
    print('result is:', result)
    print()
    
    print((5 < x) or (x < 10))
    print((5 < x) and not(x < 10))
    
    #you can summarize 'and' comparisons
    print('(5 < x < 10):', 5 < x < 10)
    print('5 < x < 10 < 99:', 5 < x < 10 < 99)
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '6.what is false?(All below)')
    print('===============================================')
    print('boolean:', False)
    print('null:', 'considered None')
    print('0:', 0)
    print('0.0:', 0.0)
    print('Empty string:', '')
    print('Empty list:', [])
    print('Empty dict:', {})
    print('Empty tuple:', tuple())
    print('Empty set:', set())
    
    
    some_list = list()
    if some_list:
        print('there is a working list.')
    else:
        print('Hey, it is empty!')
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '7.multiple comparison using in')
    print('===============================================')
    letter = 'z'
    if letter == 'a' or letter == 'e' or \
    letter == 'i' or letter == 'o' or \
    letter == 'u':
        print(letter + ' is a vowel')
    else:
        print(letter + ' is not a vowel')
        
        
    #another way using 'in'
    vowels = 'aeiou'
    letter = 'o'
    if letter in vowels:
        print(letter, 'is a vowel!')
        
    #we can use 'in' for any iterable
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    print(letter in vowel_set)
    
    vowel_tuple = ('a', 'e', 'i', 'o', 'u')
    print(letter in vowel_set)
    
    vowel_dict = {'a': 'apple',
                  'e': 'elephant',
                  'i': 'impala',
                  'o': 'ocelot',
                  'u': 'unicorn'        
                }         
    print(letter in vowel_dict)
    
          
        