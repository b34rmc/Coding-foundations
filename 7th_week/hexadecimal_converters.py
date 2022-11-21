lst =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
def dec_to_hex(dec_num):
    hexadecimal = ''
    
    while(dec_num > 0):
        remainder = dec_num % 16
        hexadecimal = lst[remainder] + hexadecimal
        dec_num = dec_num // 16
    print(hexadecimal)
dec_to_hex(int(input('enter dec to convert to hex: ')))



def hex_to_dec(hex_str):
    dec = ''
    while hex_str > 0:
        total = hex_str[-1::-1] * 16
        print(total)
hex_to_dec(input("enter hex:"))











#############################
# dec_num = int(input("Enter a number"))
# def decTo_hex(dec_num):
#     hexadecimal_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
#     hexadecimal = ''
    
#     while(dec_num > 0):
#         remainder = dec_num % 16
#         hexadecimal = hexadecimal_number[remainder] + hexadecimal
#         dec_num = dec_num // 16
#     print(hexadecimal)
# (decTo_hex(dec_num))