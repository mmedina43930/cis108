from random import randint

number = randint(0,20)
for a in range (6,0,-1):
    for cnt in range(1,a):
        print(cnt,'\t',end ='')
    print()
