#Python Program to demonstrate the working of built-in statistical functions mean(), mode(), median() by importing statistics library

import statistics

# list of positive integer numbers
data1 = []
num = int(input("Enter number of elements: "))
for i in range(num):
    data1.append(int(input("Enter element: ")))

x = statistics.mean(data1)

# Printing the mean
print("Mean is :", x)

# Printing the median
print("Median is :", statistics.median(data1))

# Printing the mode
print("Mode is :", statistics.mode(data1))