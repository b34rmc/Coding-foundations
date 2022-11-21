import sys

class shopping():
    def show_list(self):
        with open("shopping_list.txt", "r") as item:
            print(f'Your shopping list contains:\n{item.read()}\n')
            print(f'\n{self.interaction()}')
            
    def add_item(self):
        # ui = input()
        # with open("shopping_list.txt", "a") as item_add:
        #     item_add.write(ui)
        while True:
            with open("shopping_list.txt", 'a') as item_add:
                add_item = input("Type your item here: (Press enter to return to menu)? \n")
                if add_item == "":
                    break
                else:
                    item_add.write(f'{add_item}\n')
                    print(f'\n {add_item}" ')
            
    def clear_list(self):
        with open("shopping_list.txt", "w") as clear:
            clear.write("")
            
    def interaction(self):
        print('What would you like to do?\n')
        while True:
            options = input('(P)rint shopping list\n(A)dd item\n(C)lear\n(Q)uit\n').upper()
            if options == 'P':
                self.show_list()
            elif options == 'A':
                print(f'Enter item to add:{input()}')
                self.add_item()
            elif options == 'C':
                self.clear_list()
            elif options == 'Q':
                sys.exit()
    
print("\nWelcome to Matt's shopping program\n")
shop = shopping()
while True:
    question = input('would you like to create your shopping list? (y/n)\n').lower()
    if question == 'y':
        shop.interaction()
    elif question == 'n':
        print('Have a great rest of your day!')
        sys.exit()
    else:
        print('wrong command!')
    

            
    
# add items to a list
# make a function to add items to a list then append the list to a file and then read the file back.