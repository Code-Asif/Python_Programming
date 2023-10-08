#Python program to find the average of 10 numbers using while loop.

avg=0
print("Enter 10 numbers: ")
for i in range(1,11):
    avg += int(input())
avg /=10

print("Average : ",avg)