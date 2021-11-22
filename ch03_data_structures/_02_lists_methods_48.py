'''
oscar
BVH APCS Principles
'''

#imports


#functions


if __name__ ==  "__main__":
    #===========================================================================
    # 1.append() - places item to the end of the list
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo']
    marxes.append('Zeppo')
    print(marxes)
    
    #===========================================================================
    # 2.combine lists by using extend() or +=
    #===========================================================================
    others = ['gummo','Karl']
    marxes.extend(others)
    print('extend() =', marxes)
  
    #reset marxes list
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
    marxes += others
    print('+= ', marxes)
    
    #append using lists
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
    others = ['gummo','Karl']
    marxes.append(others)
    print('append a list -->', marxes)
    
    
    #===========================================================================
    # 3.insert()
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
    marxes.insert(0, 'Mr. Gracias')
    print(marxes)
    
    #No exceptions if using large index
    marxes.insert(10, "Added name")
    print('Higher index: ', marxes)
    
    
    
    #===========================================================================
    # 4.delete an item using del using listName[0]
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
    del marxes[2]
    print(marxes)
    
    #===========================================================================
    # 5.delete an item by value using remove()
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
    marxes.remove('Groucho')
    print(marxes)
    
    
    #===========================================================================
    # 6.pop()
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
    marxes.pop() #default is the last item
    print(marxes)
    
    #pop the first item index
    marxes.pop(0)
    print(marxes)
    
    #===========================================================================
    # 7.find the index using index()
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
    print(marxes.index('Chico'))
    
    #yields error since Zeppo is not found in range
#    print(marxes.index('Zeppo', 0, 2))
    
    #===========================================================================
    # 8. test for a value in
    #===========================================================================
    words = ['a', 'deer', 'a', 'female', 'deer']
    found = 'deer' in words
    print(found)
    
    
    #===========================================================================
    # 9.count occurrences using count()
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Harpo']
    print(marxes.count('Harpo'))
    
    #===========================================================================
    # 10.convert to a string with join() and split()
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo']
    print('*'.join(marxes))
    
    separator = ' - '
    days = ['Monday', 'Tuesday', 'Wednesday']
    joined_days = separator.join(days)
    print(joined_days)
    
    
    #split()
    separated = joined_days.split(separator)
    print(separated)
    
    #===========================================================================
    # 11.reorder with sort() by itself, sorted() makes an orderly copy
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo']
    sorted_marxes = sorted(marxes)
    #sorted_marxes is a copy of the original
    print(sorted_marxes)
    
    names = ['Oscar', 'Charlie', 'Felipe']
    names.sort()
    print(names)
    
    
    numbers = [3, 5, 12, 0.1, 78, 32]
    numbers.sort()
    print(numbers)
    
    numbers = [3, 5, 12, 0.1, 78, 32]
    numbers.sort(reverse=True)
    print(numbers)
    
    
    #===========================================================================
    # 12.length of a list
    #===========================================================================
    marxes = ['Groucho', 'Chico', 'Harpo']
    print(len(marxes))
    
    
    #===========================================================================
    # 13.assign with =, copy with copy()
    #===========================================================================
    a = [1, 2, 3]
    print(a)
    b = a
    print(b)
    
    #change an item in a and b changes as well
    a[0] = 'surprise'
    print(a)
    print(b)
    
    
    #copy
    c = [3, 4, 5]
    d = c.copy()
    print('c:', c)
    print('d:', d)
    
    #change first item in c
    c = [3, 4, 5]
    d = c.copy()
    print('c before:', c)
    print('d before:', d)
    c[0] = 'another surprise'
    print('c before:', c)
    print('d before:', d)
    
    
    