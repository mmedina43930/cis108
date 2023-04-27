total = 0
prompt = input("Do you have numbers to add (Y/N): ")[0].upper()
while  (prompt!= 'Y' and prompt != 'N'):
    prompt = input("Invalid Input, Re-enter (Y/N) ")[0].upper()
while (prompt[0] == 'Y'):
    number = int(input("enter an integer number : "))
    while number < 0 or number >100:
        number = int(input("Invalid number, Re-enter number please : "))
    total += number
    prompt = input("Do you have another number")[0].upper()
    while  (prompt!= 'Y' and prompt != 'N'):
        prompt = input("Invalid Input, Re-enter (Y/N) ").upper()
print ("The total is ", total)
