# Menu Class: represents the menu options that can be added/removed
class Menu:
    def __init__(self):
        self.menu_list = []
    
    # return the list of availble menu options
    def display_menu(self):
         self.menu_list = ['Add to Cart', 'Remove from Cart',\
             'Total Bill', 'Generate Invoice','Exit']
         return self.menu_list