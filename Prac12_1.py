#Python program to implement matrix multiplication.

listA = [[],[]]
print("Enter element in A matrix")
for i in range(2):
    for j in range(2):
        listA[i].append(int(input("Enter element: ")))

listB = [[],[]]
print("Enter element in B matrix")
for i in range(2):
    for j in range(2):
        listB[i].append(int(input("Enter element: ")))

listC = [[],[]]
for i in range(2):
    for j in range(2):
        listC[i].append(0)

for i in range(2):
    for j in range(2):
        for k in range(2):
            listC[i][j] += listA[i][k]*listB[k][j]
            
print("Multiplication of matrix A and B is : ")
for i in range(2):
    for j in range(2):
        print(listC[i][j], end="\t")
    print("\n")


