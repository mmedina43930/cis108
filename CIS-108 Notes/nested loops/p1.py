#A program that finds the average of  a test for multiple tests.
number_tests = 0
answer = input("do you have a test")[0].upper()
while answer == 'Y':
    total = 0
    cnt = 0
    score = float(input("Enter Score : "))
    while (score >= 0):
        total += score
        cnt += 1
        score = float(input("Enter next Score : "))
    print("Number of tests", cnt)
    print("Average = ", total/cnt)
    number_tests += 1
    answer = input("do you have aother test")[0].upper()
print("The Number of tests Averaged ",number_tests)

