total = 0.0
answer = input("Have a number?(y/n): ")[0].upper()
while answer == "Y":
   number = float(input("Enter the number : "))
   total += number
   answer = input("Another Number? : ")[0].upper()
print ("The sum is ", format(total, "7.2f"))
input("Press Enter to Continue")
