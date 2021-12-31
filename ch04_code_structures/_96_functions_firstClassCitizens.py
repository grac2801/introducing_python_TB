'''
author: oscar
date: 2021-12-31 15:28
'''

#imports


#functions
def answer():
    print(42)
    
def run_something(func):
    func()

def add_args(arg1, arg2):
    print(arg1 + arg2)
    
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


if __name__ == '__main__':
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'print answer()')
    print('===============================================')
    answer()
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'run_something() and pass a fx as argument')
    print('===============================================')
    run_something(answer)
    print('What kind is run_something?', type(run_something))
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'run a fx with arguments')
    print('TOPIC: --->', 'add_args(arg1, arg2) from within')
    print('TOPIC: --->', 'run_something_with_args')
    print('===============================================')
    run_something_with_args(add_args, 5, 9)
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', 'combine with *args and **kwargs')
    print('TOPIC: --->', 'sum_args() and run_with_positional_args()')
    print('===============================================')
    print(run_with_positional_args(sum_args, 1, 2, 3, 4))
    
    