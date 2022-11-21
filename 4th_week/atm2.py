import sys
import random

class ATM():
    def __init__(self, balance = 0):
        self.balance = balance
        
    def account_detail(self):
        print(f"Available balance: Nu.{self.balance}\n")
        
    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print('Deposit successful! Your current balance is now: ', self.balance)
        
    def withdraw(self, withdraw):
        self.withdraw = withdraw
        if self.withdraw > self.balance:
            print('Insuffecient funds!')
            print(f'The max you can withdraw is {self.balance}')
        else:
            self.balance = self.balance - self.withdraw
            print(f'Withdraw successful! Your current balance is now {self.balance}')
            
    def check_balance(self):
        print(f'Available balance: {self.balance}')
        
    def transaction(self):
        while True:
            option = input('(B)alance\n(D)eposit\n(W)ithdraw\n(Q)uit\n').upper()
            if option == 'B':
                self.check_balance()
            elif option == 'D':
                amount = int(input('Enter amount to deposit: '))
                self.deposit(amount)
            elif option == 'W':
                amount = int(input("Enter amount to withdraw:"))
                self.withdraw(amount)
            elif option == 'Q':
                print(f"""
                printing receipt..............
            ******************************************
            _________________________________________________________
            | Transaction number: {random.randint(10000, 1000000)}                            |                
            | Available balance: {self.balance}                               |     
            | Thanks for banking with the bank of Matt              |
            |_______________________________________________________|                
            ******************************************
            """)
                sys.exit()                  
                    
print('***************************\nWelcome to the bank of Matt\n***************************\n')

atm = ATM()
while True:
    trans = input("Do you want to do any transactions today?(y/n): ")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    __________________________________________
   | Thanks for banking with the bank of Matt |
   | Visit us again!                          |
   |__________________________________________|
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")