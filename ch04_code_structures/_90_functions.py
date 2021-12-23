'''
author: mrgracias
Year: 2021
'''
# imports


# functions
def main():
    print(commentary('blue'))


def commentary(color):
    if color == 'red':
        return 'it is a tomato'
    elif color == 'green':
        return 'it is a green pepper'
    elif color == 'bee purple':
        return 'I don\'t know what is it, but bees can see it'
    else:
        return 'I\'ve never heard of this color'


if __name__ == '__main__':
    main()
