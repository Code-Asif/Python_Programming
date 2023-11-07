#Python program to generate the prime numbers from 1 to N.

num = int(input("Enter num: "))
for i in range(1,num):
    count=0
    temp=i
    for j in range(2,temp):
        if(temp%j==0):
            count+=1
    if(count==0):
        print(i, end=" ")