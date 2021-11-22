'''
Oscar
BVH APCS Principles
'''

#imports


#functions


if __name__ ==  "__main__":
    #===========================================================================
    # 1.create a dictionary
    #===========================================================================
    empty_dict = {}
    print(empty_dict)
    
    food_menu = {
        'pizza': 17.95,
        'burger': 5.56,
        'small drink': 2
    }
    print(food_menu)
   
    #======================================================================
    # 2.convert to dictionary
    #======================================================================
    lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    #convert list into a dictionary
    lol_dict = dict(lol)
    print(lol_dict)
    
    
    #convert a list of tuples into a dictionary
    lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    lot_dict = dict(lot)
    print(lot_dict)
    
    #convert a list of two-character items
    duets = ['ab', 'cd', 'ef']
    duets_dict = dict(duets)
    print(duets_dict)
    
    
    
    #convert two-item character tuple into dictionary
    tos = ('ab', 'cd', 'ef')
    tos_dict = dict(tos)
    print(tos_dict)
    
    
    #===========================================================================
    # 3.add or change an item by key
    #===========================================================================
    pythons = {'Chapman': 'Graham',
               'Cleese': 'John',
               'Idle': 'Eric',
               'Jones': 'Terry',
               'Palin': 'Michael'
               }
    print(pythons)
    
    #we are missing one more, let's add it by key, and make an error as well
    pythons['Gillian'] = 'Gerry'
    print(pythons)
    
    #let's fix the value
    #If you use key more than once, last one wins
    pythons['Gillian'] = 'Terry'
    print('fixed:', pythons)
    
    #===========================================================================
    # 4.combine dictionaries with update()
    #===========================================================================
    old_friends = {'Jones': 'Omar', 'Levine': 'John'}
    print('old_friends', old_friends)
    
    new_friends = {'newby': 'Laura'}
    print('new_friends', new_friends)
    
    old_friends.update(new_friends)
    print('old_friends updated', old_friends)
    
    #another example showing last value wins
    first = {'a': 1, 'b': 2}
    second = {'b': 'platypus'}
    #update first
    first.update(second)
    print(first)
    
    #===========================================================================
    # 5.delete an item by key
    #===========================================================================
    days = {'Monday': 1, 
            'Tuesday': 2,
            'Wednesday': 3}
    print('days:', days)
    
    #delete Tuesday
    del days['Tuesday']
    print('days:', days)
    
    #===========================================================================
    # 6.delete keys using clear
    #===========================================================================
    print('days:', days)
    days.clear()
    print('days:', days)
    
    #===========================================================================
    # 7.test for a key using "in"
    #===========================================================================
    days = {'Monday': 1, 
            'Tuesday': 2,
            'Wednesday': 3}
    tuesday = 'Tuesday' in days
    print(tuesday)
    Friday = 'Friday' in days
    print(Friday)
    
    #===========================================================================
    # 8.get an item by key
    #===========================================================================
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'get an item by key')
    print('===============================================')
    days = {'Monday': 1, 
        'Tuesday': 2,
        'Wednesday': 3}
    #If key in dictionary, you get an exception
    #isFriday = days['Friday']
    #print(isFriday)
    
    #two ways to avoid this:
    #1) use the 'in' keyword
    isFriday = 'Friday' in days
    print(isFriday)
    
    #2) use of the get() function
    print(days.get('Friday', 'Key not found!!'))#custom message
    print(days.get('Friday'))#default message
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '9.get all keys using keys()')
    print('===============================================')
    signals = {'green': 'go', 'yellow': 'slow down', 'red': 'stop'}
    print(signals.keys())
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '10.get all values using values()')
    print('===============================================')
    print(list(signals.values()))
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '11.get all key,value pairs using items()')
    print('===============================================')
    print(list(signals.items()))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '12.assign with "=", copy using copy()')
    print('===============================================')
    #using assignment
    saved_signals = signals
    print('assigned saved_signals:', saved_signals)
    #change signals
    signals['blue'] = 'confuse anyone'
    print('saved_signals:', list(saved_signals.items()))
    
    #using copy()
    signals = {'green': 'go', 'yellow': 'slow down', 'red': 'stop'}
    new_signals = signals.copy()
    #now change original signals
    signals['blue'] = 'confusing!!'
    print('signals:', signals)
    print('new_signals:', new_signals)
    
    
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    

    
    
    
    
    
    
    
    
    