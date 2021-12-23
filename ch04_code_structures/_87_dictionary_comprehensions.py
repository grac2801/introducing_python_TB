'''
author: mrgracias
Year: 2021
'''
# imports

# functions

if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' count letters in a word')
    print('===============================================')
    words = 'letters'
    letter_counts = {letter: words.count(letter) for letter in words}
    print(letter_counts)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' same count letters but using long way')
    print('===============================================')
    count_dictionary = {}
    wording = "hello"
    for letter in range(len(wording)):
        count_dictionary[wording[letter]] = wording.count(wording[letter])
    print(count_dictionary)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', ' same count using a set and comprehension')
    print('===============================================')
    word = 'letters'
    letter_counts = {letter: word.count(letter) for letter in set(word)}
    print(letter_counts)

