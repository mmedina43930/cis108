total = 0
prompt = input("Do you have numbers to add : ").upper()
while (prompt[0] == 'Y'):
    number = int(input("enter an integer number : "))
    while number < 0 or number >100:
        number = int(input("Invalid number, Re-enter number please : "))
    total += number
    prompt = input("Do you have another number").upper()
print ("The total is ", total)
