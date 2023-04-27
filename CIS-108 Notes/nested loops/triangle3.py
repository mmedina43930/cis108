size = int(input("Enter Number of Rows : "))
for row in range (size, 0,-1):
    for column  in range(1, row+1):
        print(column,end = "  ")
    print()
