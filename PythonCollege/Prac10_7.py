#Python program to implement linear search
def L_Search(n, key):
    for i in range(n):
        if list[i] == key:
            print("Key found at ",i,"index")
            return
    print("Key not found")

n = int(input("Enter size of list: "))
list = []
for i in range(n):
    list.append(int(input("Enter number to add in list: ")))
key = int(input("Enter element to search: "))
L_Search(n,key)
