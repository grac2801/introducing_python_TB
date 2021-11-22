'''
@author: mrgracias
'''
#imports


#functions


if __name__ == '__main__':
    #a set is a dictionary without values. 
    #All you care about is to know whether it exists.
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '1.create a set')
    print('===============================================')
    empty_set = set()
    print(empty_set)
    
    even_numbers = {0, 2, 4, 6, 8}
    print(even_numbers)
    
    #sets like dictionaries are unordered.
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '2.convert other data into sets')
    print('===============================================')
    letters = set('letters')
    print(letters)#repeated letters only print once
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '3.let\'s make a set from a list ')
    print('===============================================')
    reindeer_list = ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']
    reindeer_set = set(reindeer_list)
    print(reindeer_set)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '4.let\'s make a set from a tuple')
    print('===============================================')
    sea_animals_tuple = ('dolphin', 'whale', 'fish', 'tuna')
    #convert to set
    sea_animal_set = set(sea_animals_tuple)
    print(sea_animal_set)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '5.When given a dict, set only uses keys')
    print('===============================================')
    fruits_list = {'apple': 'red',
              'orange': 'orange',
              'pear': 'green',
              'banana': 'yellow'}
    fruits_set = set(fruits_list)
    print('fruits_set:', fruits_set)
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '6.test for a value in set using \'in\'')
    print('===============================================')
    drinks = {'martini': {'vodka', 'vermouth'},
              'black russian': {'vodka', 'kahlua'},
              'white russian': {'cream', 'kahlua', 'vodka'},
              'manhattan': {'rye', 'vermouth', 'bitters'},
              'screwdriver': {'orange juice', 'vodka'}
              }
    print(drinks)
    
    
    #preview of for, and , or, if
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '6a.Which drinks have vodka in them?')
    print('===============================================')
    counter = 0
    for name, contents in drinks.items():
        if 'vodka'in contents:
            counter += 1
            print(counter, ' - ', name)
            
            
            
    print('') 
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '6b.Which drinks have vodka but are lactose intolerant - no Kerosene')
    print('===============================================')
    for name, contents in drinks.items():
        if 'vodka' in contents and not('vermouth' in contents or 'cream' in contents):
            print(name)
        
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '7.combinations and operations')
    print('intersection symbol: &')
    print('which drinks have vermouth or orange juice?')
    print('===============================================')
    for name, contents in drinks.items():
        if contents & {'vermouth', 'orange juice'}:
            print(name)
        
        
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '7a.Which drinks have vodka, but neither cream nor vermouth')
    print('===============================================')
    for name, contents in drinks.items():
        if 'vodka' in contents and not contents & {'cream', 'vermouth'}:
            print(name)
        
        
    #Let's save the ingredients of both white and black russian drinks
    bruss = drinks['black russian']
    wruss = drinks['white russian']
    print('bruss', bruss)
    print('wruss', wruss)
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8. set operators')
    print('TOPIC: --->', '8a.intersection() or &')
    print('===============================================')
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a & set_b)#only items in common
    print(set_a.intersection(set_b))
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8b.union or |')
    print('===============================================')
    print(set_a.union(set_b))
    print(set_a | set_b)#list all items in both
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8c.difference or -')
    print('===============================================')
    print(set_a - set_b)#member of first set but not second
    print(set_a.difference(set_b))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8c.symmetric_difference or ^')
    print('Items in one set or the other, but not both')
    print('===============================================')
    print(set_a ^ set_b)
    print(set_a.symmetric_difference(set_b))
        
    #let's apply to the russian drinks
    print(bruss.symmetric_difference(wruss))
    print(wruss.symmetric_difference(bruss))
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8d.issubset() or <=')
    print('===============================================')
    set_a = {1, 2}
    set_b = {2, 3}
    print('a subset of b?', set_a.issubset(set_b))
    #going back to the russian drinks
    print('bruss subset of wruss?', bruss <= wruss)
    
    #any set is a subset of itself
    print('set_a subset of itself?', set_a <= set_a)
    

    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8e.issuperset() or >==')
    print('===============================================')
    print('wruss >= bruss?', wruss >= bruss)
    
    
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '9.Make bigger data structures')
    print('===============================================')
    marxes = ['Groucho', 'Chico', 'Harpo']
    pythons = ['Chapman', 'Cleese', 'Gillian', 'Jones', 'Palin']
    stooges = ['Moe', 'Curly', 'Larry']
    
    #Make a tuple that contains each list as an element
    tuple_of_lists = (marxes, pythons, stooges)
    print(tuple_of_lists)
    
    #Make a list that contains each list as an element
    list_of_lists = [marxes, pythons, stooges]
    print(list_of_lists)
    
    #Make a dictionary that contains each list as an element
    dict_of_lists = {'marxes': marxes, 'pythons': pythons, 'stooges':stooges}
    print(dict_of_lists)
    
    
    #only limitation: data types
    #dict key needs to be immutable --> so list, dict or set can't be
    #keys for dictionaries, but a tuple can be
    houses = {(44.79, -93, 285): 'My house',
           (34.56, 32.98, 87): 'Aunt\'s house'
        }
    print(houses)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    