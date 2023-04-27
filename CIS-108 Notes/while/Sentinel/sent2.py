total = 0
coupons = 0
cnt1 = 0
cnt = 0
amount = float(input("Enter items cost : "))
while (amount != 0):
   total += amount
   if amount < 0:
       coupons = coupons - amount
       cnt1 +=1
   cnt += 1
   amount = float(input("Enter items cost : "))
print ("The number of items", cnt);
print ("The total is ",format(total,"6.2f"))
print ("Number of Coupons ", cnt1)
print ("Total Coupons ",coupons)
