from atm2 import ATM


print('***************************\nWelcome to the bank of Matt\n***************************\n')

atm = ATM()
while True:
    trans = input("Do you want to do any transactions today?(y/n): ")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")