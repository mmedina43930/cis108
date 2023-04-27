total = 0
cnt = 0
amount = float(input("Enter items cost : "))
while (amount != 0):
   total += amount
   cnt += 1
   amount = float(input("Enter items cost : "))
print ("The number of items", cnt);
print ("The total is ",format(total,"6.2f"))
