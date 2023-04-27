answer = input("Have a number? : ")[0].upper()
countZeros = 0
sumpositive = 0
sumnegative = 0
while (answer == 'Y'):
    number = int(input("Number? : "))
    if (number >0):
        sumpositive = sumpositive + number
    elif (number < 0):
        sumnegative -= number

    else:
        countZeros += 1
    answer = input("Have another number? : ")[0].upper() 
print("sum of positive Numbers ",sumpositive)
print("sum of negative Numbers ",sumnegative)

                 
