'''
author: oscar
date: 2021-12-31 15:52
'''

#imports


#functions
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


def knights(saying):
    def inner(quote):
        return f"we are in the knights who say: {saying}"
    return inner(saying)

if __name__ == '__main__':
    print(outer(4, 7))
    print(knights('Hi'))
    
    