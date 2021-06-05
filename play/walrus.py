''' Explore Walrus operator introduced in Python 8: https://www.python.org/dev/peps/pep-0572/ '''

import sys

def list_cats():
    print ("Enter cat's name to play\nEnter 'quit' or nothing at all to find a cat's color")
    print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

    cats = list()
    while (cat := input('Write cat name: ')) not in  ('quit', ''):
        cats.append(cat)
    print(f'List of cats: {cats}')

def cat_color(cat_name='Nemo'):
    if color := what_color(cat_name):
        print(f'{cat_name} is all or mostly {color}.')
        return
    print(f"{cat_name}'s color is unknown.")

def what_color(cat_name):
    if cat_name in ('Nemo', 'Ninja'):
        return 'black'
    if cat_name in ('Ronin', 'Sammy', 'Mac'):
        return 'orange'
    if cat_name in ('PD', 'Greyface'):
        return 'gray'

def pick_cat_name(options):
    print('Please choose cat name:')
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    i = input('Enter number: ')
    try:
        if 0 < int(i) <= len(options):
            return int(i)
    except:
        sys.exit('Exiting becauee of error.  Usage: select a number that is displayed on the screen')
    return None
