number = float(input("Enter a float,0 to stop:"))
total = 0.0
while number >= 0:
    total += number
    number = float(input("Enter a float 0 to stop : "))
print ("The sum is ", format(total, "7.2f"))
input("Press Enter to Continue")
