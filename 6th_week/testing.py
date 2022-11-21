def binaryProduct(biNum1, biNum2):
    i = 0
    remainder = 0
    sum = []
    binaryProd = 0
    binaryMultiply = 0
    factor = 1
        
        
# while the input isn't just '0', run the rest.
    while biNum1 != 0 or biNum2 != 0:
        sum.insert(i, (((biNum1 % 10) + (biNum2 % 10) + remainder) % 2))
        remainder = int(((biNum1 % 10) + (biNum2 % 10) + remainder) / 2)
        biNum1 = int(biNum1/10)
        biNum2 = int(biNum2/10)
        i = i+1
  
    #loop to check if theres a number and if so, keep multiplying
    while biNum2 != 0:
        digit = biNum2 % 10
        if digit == 1:
            biNum1 = biNum1 * factor
            binaryMultiply = binaryProduct(biNum1, binaryMultiply)
        else:
            biNum1 = biNum1 * factor
        biNum2 = int(biNum2/10)
        factor = 10
    
    # if the remainder isn't zero, insert into equation.
    if remainder != 0:
        sum.insert(i, remainder)
        i = i+1
    i = i-1
    while i >= 0:
        binaryProd = (binaryProd * 10) + sum[i]
        i = i-1
    return "\nMultiplication Result = " + str(binaryProd)
  
num1 = int(input('1:'))  
num2 = int(input('2:'))
print(binaryProduct(num1, num2))