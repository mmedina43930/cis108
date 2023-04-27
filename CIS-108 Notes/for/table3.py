SIZE = 12
print("\t\t\tMultiplication Table")
print(format("|",">5s"),end = "")
for j in range(1,SIZE+1):
    print(format(j,"<5d"), end = "")
print()
print("------" * SIZE)
for i in range (1,SIZE+1):
    print(format(i,"<2d"), "|", end = "")
    for j in range(1,SIZE+1):
        print(format(i*j, "<5d"), end = "")
    print()
