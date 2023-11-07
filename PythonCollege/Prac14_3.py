#Python Program to Swap the First and Last Element in a List.

def swapFL(list, n):
    if n == 1:
        return list
    else:
        temp = list[0]
        list[0] = list[n-1]
        list[n-1] = temp
        return list
    
list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    list.append(int(input("Enter element: ")))
    
print("List after swapping first and last elements:", swapFL(list, len(list)))

