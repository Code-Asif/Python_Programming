#Python program to implement binary search.

def binary_Search(n, key):
    low = 0
    high = n-1
    while low <= high:
        mid = int((low+high)/2)
        if(key > list[mid]):
            low = mid + 1
        if(key < list[mid]):
            high = mid - 1
        if (key == list[mid]):
            print("Key found at", mid,"index")
            return
    print("Key not found")

list = []
n = int(input("Enter size of list: "))
for i in range(n):
    list.append(int(input("Enter n to add in list: ")))

key = int(input("Enter element to search: "))
binary_Search(n, key)