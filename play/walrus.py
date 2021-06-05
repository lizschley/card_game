''' Explore Walrus operator introduced in Python 8: https://www.python.org/dev/peps/pep-0572/ '''

def list_cats():
    print ("Type 'quit' to quit!")
    print ('^^^^^^^^^^^^^^^^^^^^')

    cats = list()
    while (cat := input('Write cat name: ')) != 'quit':
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
