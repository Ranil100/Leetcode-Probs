def rev_num(n):                                    # reverse a num
    s=0                
    while n>0:
        r=n%10
        s=s*10 + r
        n=n//10

    print(s)


rev_num(147)


def prime_num(n):                                 # prime num

    if n <= 1:
        return "invalid num"

    for i in range(2, n):
        if n % i == 0:
            return "no"

    return f"{n}is a prime num"


print(prime_num(7))


def fibbonacci(n):                                 # fibbonacci
    a,b=0,1
    for i in range(n):
        a,b = b,a+b
    print(b)
    
fibbonacci(5)      

def Second_max(list):                             # second largest num
    first = second = -99999
    for i in list:
        if i>first:
            second = first
            first = i
        elif i>second and i!= first:
            second = i
    print (second)
    
Second_max([1,2,3,4,5])    

def arr_rev(arr):                                # reverse a array
    left = 0
    right = len(arr)-1
    
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        
        left+=1
        right-=1
    print (arr)

arr_rev([1,2,3,4,5])   

def count_occurences(arr,key):                   # count occurences
    count =0
    for i in arr:
        if i == key:
            count+=1
    
    print(f"{key} occured {count} times")        
    
count_occurences([1,2,1,1,3],1) 



n = 10                                            # Decimal to Binary
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print(binary)


binary = "1010"                                   # Binary to Decimal
decimal = 0
power = 0

for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print(decimal)

     
year = 2024                                      # Leap year

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")


n = 145                                         # Strong Number
original = n
sum_val = 0

while n > 0:
    digit = n % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_val += fact
    n //= 10

print("Strong Number" if sum_val == original else "Not Strong")

  
n = 123456                                              # count num of odd and even nums in the digit

even = 0
odd = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n //= 10

print("Even:", even)

n = 5                                                  #Find Sum of Squares
sum_sq = 0

for i in range(1, n + 1):
    sum_sq += i * i

print(sum_sq)
print("Odd:", odd)




