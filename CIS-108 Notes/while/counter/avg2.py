count = 0
total = 0
numstud = int(input("How Many Students took the test "))
while (count < numstud):
    test = float(input("Enter test : "))
    total = total + test
    count += 1
average = total / (count)
print(average)
