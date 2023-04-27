number = int(input("Number? - 0 to stop : "))
counter = 0
sumpositive = 0
sumnegative = 0
while (number != 0):
    counter += 1
    if (number >0):
        sumpositive = sumpositive + number
    else:
        sumnegative -= number
    number = int(input("Number? - 0 to stop : "))
print("sum of positive Numbers ",sumpositive)
print("sum of negative Numbers ",sumnegative)

                 
