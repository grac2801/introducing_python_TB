'''
oscar
BVH APCS Principles
'''

#imports


#functions


if __name__ ==  "__main__":
    fact = 'Tuples are immutable'
    
    #===========================================================================
    # 1.empty tuple()
    #===========================================================================
    emtpy_tuple = ()
    print(emtpy_tuple)
    
    #===========================================================================
    # 2.making tuples
    #===========================================================================
    friends = ('Rob', 'Nancy', "Esther")
    print(friends)
    
    #you don't need parenthesis
    animals = 'giraffes', 'lions', 'fishes'
    print(animals)
    print(type(animals))
    
    #===========================================================================
    # 2.Assign multiple values to multiple variables
    #===========================================================================
    trees = ('cedar', 'oak', 'lemon') 
    a, b, c = trees #tuple unpacking
    print(a)
    print(b)
    print(c)
    
    password = 'swordfish'
    ice_cream = 'chocolate'
    print('password:', password, 'ice_cream:', ice_cream)
    password, ice_cream = 'chocolate', 'swordfish'
    print('password:', password, 'ice_cream:', ice_cream)
    
    #===========================================================================
    # 3.tuple() function
    #===========================================================================
    marx_list = ['Groucho', 'Chico', 'Harpo']
    to_tuple = tuple(marx_list)
    print(to_tuple)
    
    
    #===========================================================================
    # Tuples vs lists:
    # a) tuples use less space
    # b) can't change tuples by error
    # c) you can use tuples as keys in dictionaries
    # d) can be passes as arguments in functions
    #===========================================================================
    
    
    
    
    
    