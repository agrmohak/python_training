start = int(input('Enter start num'))
end = int(input('Enter end num'))
if(start<1 or end<1):
    print('Please check range(start and end be greater than 1)')
    exit()

def check_prime(num):
    if(num==1):
        return False
    
    for x in range(2,num//2+1):
        if(num%x==0):
            return False
    return True

def find_primes(start,end):
    for x in range(start,end+1):

        if(check_prime(x)):
            print(x)
