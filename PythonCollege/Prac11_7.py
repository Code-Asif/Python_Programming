#Python program to implement matrix addition.

print("Enter element in A matrix")
A = [[],[]]
for i in range(2):
    for j in range(2):
        A[i].append(int(input("Enter element: ")))
        
print("Enter element in B matrix")
B = [[],[]]
for i in range(2):
    for j in range(2):
        B[i].append(int(input("Enter element: ")))
        
sum =[[],[]]
for i in range(2):
    for j in range(2):
        sum[i].append(A[i][j]+B[i][j])
        
print("Sum of matrix A and B is : ")
for i in range(2):
    for j in range(2):
        print(sum[i][j], end="\t")
    print("\n")


