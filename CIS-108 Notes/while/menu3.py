import os

choice = 5
while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
    os.system("CLS")
    print("\t\tMajor Options")
    print("\t\t-------------\n")
    print("\t 1- Business")
    print("\t 2- CIS")
    print("\t 3- English")
    print("\t 4- Math")
    choice = int(input("\t\tEnter Choice : "))
if (choice == 1):
    print("\n\nBusiness Major Declared")
elif (choice == 2):
    print("\n\nCIS Major Declared")
elif (choice == 3):
    print("\n\nEnglish Major Declared")
elif (choice == 4):
    print("\n\nMath Major Declared")
print("All done")
input("Press Enter To Continue")
