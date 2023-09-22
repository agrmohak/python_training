numInputs = int(input('Enter number of numbers'))
if(numInputs<2):
    print("Need atleast 2 numbers")
    exit()

maxNum = int(input(f"Enter Number {1}: "))
maxNum2 = None


for x in range(2, numInputs+1):
    num = int(input(f"Enter Number {x}: "))
    if(int(num)>maxNum):
        maxNum2 = maxNum
        maxNum=int(num) 
    if(maxNum2==None or int(num)>maxNum2) and int(num)<maxNum:
        maxNum2 = int(num)

if(maxNum2==maxNum):
    print("No 2nd Largest numebr is present")
else:
    print(maxNum2)