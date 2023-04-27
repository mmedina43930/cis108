size = int(input("Enter Number of Rows : "))
for row in range (1,size+1):
     print("   "*(size - row),end = "")
     for column  in range(1,row+1):
          print(column, end = "  ")
     print()
