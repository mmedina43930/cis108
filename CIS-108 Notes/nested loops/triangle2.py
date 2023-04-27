input("Press Enter to Continue")
size = int(input("Enter Number of Rows : "))
for row in range (1,size+1):
    for column  in range(row,0,-1):
        print(column,end = " ")
    print()
