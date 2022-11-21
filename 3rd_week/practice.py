class car():
    def __init__(self, brand, model, hp, color):
        self.brand = brand
        self.model = model
        self.hp = hp
        self.color = color
        
    def display(self):
        print('This car is a' [self.brand], [self.model], 'with' [self.hp],'hp, and comes in a stunning' [self.color], 'color')
bmw = car('BMW', 'M3', '333', 'White')
toyota = car('Toyota', 'Supra', '333', 'Black')
audi = car('Audi', 'R8', '560', 'White')    

bmw.display()
toyota.display()
audi.display()
# import platform  # For getting the operating system name
# import subprocess  # For executing a shell command


# def clear_screen():
#     """Clears the terminal screen."""

#     # Clear command as function of OS
#     command = "cls" if platform.system().lower() == "windows" else "clear"

#     # Action
#     return subprocess.call(command) == 0


# MENU_OPTIONS = ["add item", "see your shopping list", "exit"]


# def get_user_menu_choice() -> int:
#     """Gives the user a menu to choose from"""
#     low, high = 1, len(MENU_OPTIONS)
#     error_msg = f"Woops, your input must be an integer in {low}...{high}\n"
#     while True:
#         print("Input a number from the list below:")
#         for index, option in enumerate(MENU_OPTIONS):
#             print(f" {1+index:>3d}: {option}")
#         try:
#             choice = int(input("\nPlease enter a number: "))
#             if low <= choice <= high:
#                 return choice
#         except ValueError:
#             pass
#         print(error_msg)


# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add(self, item: str):
#         """Create a function that adds an item to the list"""
#         if item != "":
#             self.items.append(item)
#         return item

#     def get_items_from_user(self) -> None:
#         clear_screen()
#         print("\n\n\nWrite in the item you want to add to your shopping list!")
#         print("[leave blank to return to menu]\n")

#         item = self.add(input("> "))
#         while item:

#             clear_screen()
#             print(f"{item} was added to your shopping list!")
#             item_str = "items" if len(self.items) > 1 else "item"
#             print(f"You have {len(self.items)} {item_str} in your list.")

#             print("\nWrite in the item you want to add to your shopping list!")
#             print("[leave blank to return to menu]\n")

#             item = self.add(input("> "))

#     def __str__(self) -> str:
#         """Create a function to show all the items in the shopping list"""
#         string = "My Shopping List:\n"
#         for index, item in enumerate(self.items):
#             string += f"\n{1+index:>3d}. {item}"
#         return string + "\n"


# def main() -> None:

#     choice, add_item, display_items, exit_program = 0, 1, 2, 3

#     cart = ShoppingCart()

#     clear_screen()
#     while choice != exit_program:
#         choice = get_user_menu_choice()
#         if choice == add_item:
#             cart.get_items_from_user()
#             clear_screen()
#         elif choice == display_items:
#             clear_screen()
#             print(cart)


# if __name__ == "__main__":
#     main()
  