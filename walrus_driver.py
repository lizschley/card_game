'''
     driver for walrus operator

     Usage
     >>> python walrus_driver
'''
from play import walrus

CAT_NAMES = ('Nemo', 'PD', 'Greyface', 'Mac', 'Sammy', 'Ninja', 'Ronin')

if __name__ == "__main__":
    print('------------ New Game ------------------ ')
    print('List Cats:')
    walrus.list_cats()
    print(' ')
    print('Find Cat Color:')
    (cat_idx := walrus.pick_cat_name(CAT_NAMES) - 1)
    walrus.cat_color(CAT_NAMES[cat_idx])
