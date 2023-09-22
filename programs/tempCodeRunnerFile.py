numInputs = int(input('Enter number of numbers'))
if(numInputs<2):
    print("Need atleast 2 numbers")
    exit()

maxNum = int(input("Enter Number: "))
maxNum2 = int(input("Enter Number: "))

if(maxNum2>maxNum):
    temp = maxNum2
    maxNum2 = maxNum
    maxNum = temp

for x in range(2,numInputs):
    num = int(input("Enter Number: "))
    if(int(num)>maxNum):
        maxNum2 = maxNum
        maxNum=int(num)
    if(int(num)>maxNum2 and int(num)<maxNum):
        maxNum2 = int(num)

if(maxNum2==maxNum):
    print("No 2nd Largest numebr is present")
else:
    print(maxNum2)