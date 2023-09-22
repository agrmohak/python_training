numInputs = int(input('Enter number of numbers'))

maxNum = int(input("Enter Number: "))


for x in range(1,numInputs):
    num = int(input("Enter Number: "))
    if(int(num)>maxNum):
        maxNum=int(num)
        
print(maxNum)