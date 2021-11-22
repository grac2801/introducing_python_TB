'''
oscar
BVH APCS Principles
'''

#imports


#functions


if __name__ ==  "__main__":
    #===========================================================================
    # 1.Make lists
    #===========================================================================
    empty_list = []
    weekdays = ['Monday', 'Tuesday']
    another_empty_list =  list()
    #Items don't have to be unique
    names = ['John', "Fred", 'Fred']
    
    #Print the lists
    print(empty_list)
    print(weekdays)
    print(another_empty_list)
    print(names)
    
    
    #===========================================================================
    # 2.Convert other data type to lists
    #===========================================================================
    cat = list('cat')
    print(cat)
    
    #tuple to list
    a_tuple = ('one', 'two', 'three')
    print(a_tuple)
    tuple_to_list = list(a_tuple)
    print(tuple_to_list)
    
    #split()
    my_birthday = '03/10/1971'
    split_birthday = my_birthday.split('/')
    print(split_birthday)
    
    splitme= 'a/b//c/d///e'
    #Split by '/'
    splitme_smaller = splitme.split('/')
    print(splitme_smaller)
    
    #Split by '/'
    splitme_double = splitme.split('//')
    print(splitme_double)
    
    #===========================================================================
    # 3.Get item by offset
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo']
    print(marxes[0])
    print(marxes[1])
    print(marxes[2])
    #backwards
    print('\n--backwards')
    print(marxes[-1])
    print(marxes[-2])
    print(marxes[-3])
    
    #===========================================================================
    # 4.lists of lists
    #===========================================================================
    small_birds = ['hummingbird', 'finch']
    extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian blue']
    carol_birds = [3, 'French hens', '2', 'turtle doves']
    all_birds = [small_birds, extinct_birds, carol_birds]
    print(all_birds)
    
    #look at the first list only
    print(all_birds[0])
    #second item in first list only.
    print(all_birds[0][1] + ' is the second item of the small_birds list.')
    
    #===========================================================================
    # 5.change an item by offset
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo']
    marxes[2] = 'Wanda'
    print(marxes)
    
    #===========================================================================
    # 6.get a slice to extract item by offset range
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo']
    print(marxes[0:2])#last value is not inclusive
    
    #default step is 1 unless specified
    new_list = marxes[::2]
    print('slice:', new_list)
    
    #print list backwards
    print('backwards:', marxes[::-1])
    
    
    
    