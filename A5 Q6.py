ran1 = int(input("Enter the range for prime numbers "))



for a in range(ran1+1):
    count = 0
    for i in range(2,a):
        if a%i!=0:
            count+=1
    if count == a-2:
        print(a,"is a prime number")
    else:
        print(a,"is not a prime number")
