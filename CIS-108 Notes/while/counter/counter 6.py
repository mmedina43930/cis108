from random import randint

count = 0
correct = 0;
while count < 5 :
    first = randint(0,9)
    second = randint(0,9)
    if first < second:
        first, second = second, first
    difference = first - second
    print("\n\n",first,"-",second,"=",end =" : ")
    answer = int(input())
    if difference == answer:
        correct += 1
    count += 1
print ("The number of correct answers = ", correct)
input("Press Enter to Continue")
