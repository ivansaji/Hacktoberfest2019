# /bin/python3

def prime(num):
    #Function for checking prime
    num = int(num)
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
            
                print(num , 'not a prime')
                break
                
            
        else:
            print(num ,'is prime')
                

    else :
        print(num , 'is Not Prime')
        
def palindrome(num):
    length = len(num)
    num = int(num)
    a = list(str(num))
    for i in range(0,length):
        if a[i] == a[length-i-1]:
            print(num ,' is palindrome')
            break
        else:
            print(num , 'not palindrome')

# Beginning of Execution
for x in range (1,10000):
    prime(x)
    palindrome(str(x))