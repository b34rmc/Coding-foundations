def clear0(bin_num):
    count = 0
    max_len = len(bin_num)
    for i in bin_num:
        if i == '0':
            count += 1
        else:
            break

    new_string = ''
    for i in range(count,max_len):
        new_string = f"{new_string}{bin_num[i]}"

    return(new_string)

def bin_to_dec(bin_str):
    binary_list = []
    for i in bin_str:
        binary_list.append(i)
        
    dec_num = 0
    
    counter = 2 ** (len(binary_list) - 1)
    
    for i in binary_list:
        if i == "1":
            dec_num += counter
            counter -= counter/2
        else:
            counter -= counter/2
    
    return (f'{dec_num:.0f}')

def dec_to_bin(dec_num):
    bin_list = []
    counter = 1

    while counter < dec_num:

        counter *= 2

    while True:

        if dec_num // counter >= 1:
            
            bin_list.append('1')
            dec_num -= counter
            counter -= counter/2
            
        elif dec_num == 0 and counter < 1:
            break

        else:
            bin_list.append('0')
            counter -= counter/2


    return ''.join(bin_list)  

def bin_add(bin_input1, bin_input2):
    
    count = 0
    carry = 0
    val1_list = []
    val2_list = []

    #convert binary number to a list in reverse order
    for i in bin_input1[-1::-1]:
        val1_list.append(i)
    for i in bin_input2[-1::-1]:
        val2_list.append(i)

    #Determine how many times to run
    if len(bin_input2) > len(bin_input1):
        loop_length = len(bin_input2)
        zeros_to_add = len(bin_input2) - len(bin_input1)

        for i in range(zeros_to_add):
            val1_list.append('0')

    elif len(bin_input1) > len(bin_input2):
        loop_length = len(bin_input1)
        zeros_to_add = len(bin_input1) - len(bin_input2)
        for i in range(zeros_to_add):
            val2_list.append('0')
    
    else:
        loop_length = len(bin_input1)

    result = ''

    #Run until longest number is done.
    while count < loop_length:
        
        bin_one = val1_list[count]
        bin_two = val2_list[count]
        bin_sum = int(bin_one) + int(bin_two) + carry

        count += 1

        if bin_sum == 1:
            result += '1'          
            carry = 0
            continue

        if bin_sum == 0:
            result += '0'
            carry = 0
            continue

        if bin_sum == 2:
            result += '0'
            carry = 1
            continue

        if bin_sum == 3:
            result += '1'
            carry = 1
            continue

        

    #return result reversed to make it correct in output
    if carry > 0:
        result += '1'
    return result[-1::-1]


def bin_sub(val1, val2):
    val1_rev = []
    val2_rev = []
    borrow = False
    borrow_count = 1
    count = 0
    result = []
    max_length = max(len(val1), len(val2))

    val1 = val1.zfill(max_length)
    val2 = val2.zfill(max_length)

    for i in val1[-1::-1]:
        val1_rev.append(i)
    for i in val2[-1::-1]:
        val2_rev.append(i)

    while count < len(val1_rev):

        if borrow == True:
            
            #first run of borrow will always result in 1
            if borrow_count == 1:
                result.append(1)
                count += 1
                borrow_count += 1
                continue
        
            #stop borrowing when reaching a 1 and val2 is 0. This value will always result in a zero
            elif val1_rev[count] == '1' and val2_rev[count] == '0':
                result.append(0)
                count += 1
                borrow = False
                borrow_count = 1
                continue

            #if val1 is 1 while borrrowing, but val2 is also 1, reset borrow_counter and start again. Mathematically speaking, Val1 would have become 0 when borrowed.
            elif val1_rev[count] == '1' and val2_rev[count] == '1':
                borrow_count = 1
                continue

            #when borrowing, if values are equivalent, they will always result in 1
            elif val1_rev[count] == '0' and val2_rev[count] == '0':
                result.append(1)
                count += 1
                borrow_count += 1
                continue
            
            #when borrowing, if values are not equivalent, they will always result in 0
            else:
                result.append(0)
                count += 1
                borrow_count += 1
                continue


        #excluding borrowing, if values are equivalent, they will always result in 0
        elif val1_rev[count] == val2_rev[count]:
            result.append(0)
            count += 1
            continue
        
        #excluding borrowing, if val1 is larger but not equivalent, it will always result in 1
        elif val1_rev[count] > val2_rev[count]:
            result.append(1)
            count += 1
            continue

        #if not borrowing and val1 is smaller than val2, we need to turn on borrowing
        else:
            borrow = True
            borrow_count = 1
            
    bin_str = ''
    total_result = []
    for i in result[-1::-1]:
        total_result.append(i)
    
    for i in total_result:
        bin_str = bin_str + str(i)

    
    return clear0(bin_str)

def bin_mult(input1, input2):

    counter = 0
    current = '0'
    past = '0'
    
    max_length = max(len(input1), len(input2))
    input1 = input1.zfill(max_length)
    input2 = input2.zfill(max_length)


    for i in input2[-1::-1]:
        if i == '1':  
            current = input1 + ('0')* counter
        else:
            current = '0'
     
        past = (bin_add(past, current))
        counter += 1
       
    return past

def bin_div(val1, val2):
    count = 1
    ans = val1
    val2_dec = bin_to_dec(val2)

    while int(bin_to_dec(bin_sub(ans,val2))) >= int(val2_dec):

        ans = bin_sub(ans,val2)
        count += 1
        
    remainder = bin_sub(val1,bin_mult(val2,dec_to_bin(count)))
    result = dec_to_bin(count)       
    return f"{result} Remainder: {remainder}"

print(bin_div('101', '10'))


def interface():
    while True:
        print(
            '''\n\n*** Binary Calculator ***\n___________________________\n\n(B)inary to Decimal Conversion
(D)ecimal to Binary Conversion\n\n(A)dd two Binary Numbers\n(S)ubtract two Binary Numbers
(M)ultiply two Binary Numbers\n D(i)vide two Binary Numbers\n(Q)uit'''
            )
        display = input('').upper()
        if display == 'B':
            bin_str = input('Enter binary num to convert to int:\n')
            print(bin_to_dec(bin_str))
        elif display == 'D':
            dec_num = int(input('Enter int to convert to binary:\n'))
            print(dec_to_bin(dec_num))
        elif display == 'A':
            bin_input1 = input('Enter first number:\n')
            bin_input2 = input('Enter second number:\n')
            print(bin_add(bin_input1, bin_input2))
        elif display == 'S':
            val1 = input('Enter first number:\n')
            val2 = input('Enter second number:\n')
            print(bin_sub(val1, val2))
        elif display == 'M':
            num1 = input("Enter first binary number to multiply: ")
            num2 = input("Enter second Binary number to multiply: ")
            print(bin_mult(num1, num2))
        elif display == 'I':
            val1 = input('Enter first number:\n')
            val2 = input('Enter second number:\n')
            print(bin_div(val1, val2))
        elif display == 'Q':
            break
interface()