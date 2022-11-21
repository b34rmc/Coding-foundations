# #matt
# def decimalToBinary(num):
#     if num>1:
#         decimalToBinary(num//2)
#         result = f'{num % 2, end=''}'

# number = int(input('Enter any decimal number: '))
# decimalToBinary(number)

# #blake
# def decimalToBinary(num):
#     new_str = ""
#     while num != 0:
#         if num>1:
#             decimalToBinary(num//2)
#             result = f"{new_str}{num%2}"
#             print(result)
#             # print(num % 2, end='')

# number = int(input('Enter any decimal number: '))
# decimalToBinary(number)

# # num_0 = 8 - len(result)
# # new_string = f"{"0"*{num_0}}{result}"

# #jacob

# def dec_to_bin(dec_num):
#     if dec_num == 0:
#         return ''
#     else:
#         conversion = dec_to_bin(dec_num//2) + str(dec_num%2)
#         return conversion[0:8]
    
    
# dec_to_bin(dec_num)



# def intoBinary(number):
# #     binarynumber=""
# #     if (number!=0):
# #         while (number>=1):
# #             if (number %2==0):
# #                 binarynumber=binarynumber+"0"
# #                 number=number/2
# #             else:
# #                 binarynumber=binarynumber+"1"
# #                 number=(number-1)/2

# #     else:
# #         binarynumber="0"

# #     num = "".join(reversed(binarynumber))
# #     length = (len(num))
# #     num_0 = (8 - length)
# #     result = (f'{"0" * num_0}{num}')

# #     return result

# # print(intoBinary(244))

# def intoBi():
#     string = ''
#     number = int(input('Enter number: '))
#     if number!=0:
#         while number>=1:
#             if number % 2 == 0:
#                 string = string + "0"
#                 number = number / 2
#             else:
#                 string = string + "1"
#                 number = (number - 1) / 2
#     else:
#         string = "0"
        
#     num = ''.join(reversed(string))
#     length = len(num)
#     num_0 = 8 - length
#     result = f'{"0" * num_0}{num}'
    
    
#     print(result)

# intoBi()


# def intoInt():
#     biNum = input("Enter binary number: ")
#     counter = len(biNum)
#     total = 0
#     countUp = 1

#     while counter > 0:
#         check = biNum[counter - 1]
#         if check == '1':
#             total += countUp
#         countUp = countUp * 2  
#         counter -= 1
    
#     print(total)
        
# intoInt()