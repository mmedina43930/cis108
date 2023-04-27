grade = input("Enter Course Grade : ")[0].upper()
while (grade!= 'A' and grade != 'B'and grade!= 'C' and grade != 'D' and grade != 'F'):
    grade = input("Invalid Grade, Re-enter A, B, C, D or F : ")[0].upper()
