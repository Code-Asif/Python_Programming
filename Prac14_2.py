#Python Program to Remove Duplicates from a List.

def removeDuplicates(list):
    if len(list) == 1:
        return list
    else:
        if list[0] in list[1:]:
            return removeDuplicates(list[1:])
        else:
            return [list[0]] + removeDuplicates(list[1:])
        
list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    list.append(int(input("Enter element: ")))

print("List after removing duplicates:")
print(removeDuplicates(list))
