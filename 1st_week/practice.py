# num1 = int(input('enter number: '))
# num2 = int(input('enter number:'))
# total = f'{num1} times {num2} is {num1 * num2}'
# print(num1)
# print(num2)
# print(total)

# def greet_world():
#     print('Hello, World!')
# greet_world()


# def add_two_numbers(x, y):
#     total = x * y
#     return total
# sum = add_two_numbers(5, 5)
# print(sum)


# def maximum(x, y):
#     total = x * y
#     return total
# val = int(input('enter number: '))
# val1 = int(input('enter number: '))
# val2 = int(input('enter number: '))
# val3 = int(input('enter number: '))
# sum = f'{val} times {val1} times {val2} times {val3} is {val * val1 * val2 * val3}'
# print(sum)

    
# def average(a, b, c, d, e):
#     total = a + b + c + d + e
#     return total / 5
# a = int(input('enter number to get average: '))
# b = int(input('enter number to get average: '))
# c = int(input('enter number to get average: '))
# d = int(input('enter number to get average: '))
# e = int(input('enter number to get average: '))
# sum = a + b + c + e + d
# av = sum / 5
# print(f'the sum is {sum} and the average of the 5 numbers is {av}')

# def append_four(parameter_list):
#     parameter_list.append(4)
    
# original_list = [1, 2, 3]
# print(f'{original_list}')

# append_four(original_list)
# print(original_list)

# def maximum(a, b, c, d):
#     total = a + b + c + d
#     return print(total)

# maximum(5, 7, 8 , 12)

# def even_odd(x):
#     if (x % 2 == 0):
#         print('even')
#     else:
#         print("odd")

# list = ['cars', 'boats', 'bikes']
# print(list)
# print(list[1])

# def give_me_three(array):
#     for num in array:
#         if num == 3:
#             return num
#     print(array)
# print(give_me_three([1, 2, 4, 5]))

# def check_balance(balance_modifier):
#     user_balance = balance_modifier + balance_history[0]
#     balance_history.insert(0, user_balance)
#     return user_balance


# def deposit_choice(deposit_input):
#     while True:
#       try:
#         deposit_input = float(deposit_input)
#         if deposit_input < 0:
#           print("Invalid response. Must be a positive amount.\n")
#           break
#         else:
#           print(f'You have deposited: ${deposit_input:,.2f}')
#           print(f'Your balance is now: ${check_balance(deposit_input):,.2f}\n')
#           return False
#       except:
#         print("Invalid response. Non-numeric/non-decimal characters not allowed.\n")
#         break
#     return True


# def withdrawal_choice(withdrawal_input):
#     while True:
#       try:
#         withdrawal_input = float(withdrawal_input)
#         if withdrawal_input > balance_history[0]:
#           print(f"This amount exceeds your balance of ${balance_history[0]:,.2f}\n")
#           break
#         elif withdrawal_input == 0:
#           print("\n")
#           return False
#         elif withdrawal_input < 0:
#           print("Invalid response. Must be a positive amount.\n")
#           break
#         else:
#           print(f'Please take your ${withdrawal_input:,.2f}.')
#           negative_withdrawal = withdrawal_input * -1
#           print(f'Your balance is now: ${check_balance(negative_withdrawal):,.2f}\n')
#           return False
#       except:
#         print("Invalid response. Non-numeric/non-decimal characters not allowed.\n")
#         break
#     return True


# def menu_choice(user_choice):
#     if user_choice.upper() == "B":
#         print(f'Your balance is: ${check_balance(0):,.2f}\n')
#         return True
#     elif user_choice.upper() == "D":
#       while True:
#         if deposit_choice(input("How much would you like to deposit? $")) == True:
#           continue
#         else:
#           break
#       return True
#     elif user_choice.upper() == "W":
#       while True:
#         if withdrawal_choice(input("How much would you like to withdraw? (0 to cancel): $")) == True:
#           continue
#         else:
#           break
#       return True
#     elif user_choice.upper() == "Q":
#       print("\nThank you! Please come again!")
#       return False
#     else:
#       print("Invalid repsonse.\n")
#       return True
  

# #-------------------------------------

# print("Hello and Welcome to Mike's Bank of Python!\n")

# balance_history = [0]

# while True:
#   print("Please select from the following menu options:")
#   print("(B)alance")
#   print("(D)eposit")
#   print("(W)ithdraw")
#   print("(Q)uit")
  
#   if menu_choice(input("\nResponse: ")) == True:
#     continue
#   else:
#     break