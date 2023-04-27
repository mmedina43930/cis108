n1 = int(input("enter first integer : "))
n2 = int(input("enter second integer : "))
gcd = 1
k = 2
while k <= n1 and k <=n2:
    if n1 % k ==0 and n2 % k == 0:
        gcd = k
    k += 1
print ("The Greatest Common Divisor for",n1, "and" ,n2, "is", gcd)
