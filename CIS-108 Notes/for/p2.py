total = 0
for val in range(5):
    test = int(input("Enter test " + str(val+1)+" : "))
    while (test<0 or test > 100):
        test = int(input("Invalid test, Re-Enter " + str(val+1)+" : "))  
    total += test
average = total / (val+1)
print (average)
