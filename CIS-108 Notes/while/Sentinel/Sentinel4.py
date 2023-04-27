number = int(input("Number? - 0 to stop : "))
counter = 0
sumnums = 0
while (number != 0):
    counter += 1
    sumnums = sumnums + number
    number = int(input("Number? - 0 to stop : "))
print("Number of numbers ",counter)
print("Total numbers =", sumnums)
                 
