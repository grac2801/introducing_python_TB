'''
author: mrgracias
Year: 2021
'''
# imports

# functions

if __name__ == '__main__':
    words = 'letters'
    letter_counts = {letter: words.count(letter) for letter in words}
    print(letter_counts)
