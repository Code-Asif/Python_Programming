#Python Program to Print Largest Even and Largest Odd Number in a List

def findLargestEvenOdd(list):
    if len(list) == 1:
        if list[0]%2 == 0:
            return list[0], 0
        else:
            return 0, list[0]
    else:
        even, odd = findLargestEvenOdd(list[1:])
        if list[0]%2 == 0:
            if list[0] > even:
                return list[0], odd
            else:
                return even, odd
        else:
            if list[0] > odd:
                return even, list[0]
            else:
                return even, odd
            
list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    list.append(int(input("Enter element: ")))

even, odd = findLargestEvenOdd(list)
print("Largest even number in the list:")
print(even)
print("Largest odd number in the list:")
print(odd)
