#Python program to display all integers within the range 100-200 whose sum of digits is an even number.

for i in range(100, 200):
    temp=i
    sum=0
    while temp!=0:
        digit=temp%10
        sum += digit
        temp //=10
    if(sum%2==0):
        print(i, end=" ")