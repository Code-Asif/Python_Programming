#Python program to implement matrix addition.

print("Enter element in A matrix")
A = [3][3]
for i in range(3):
    for j in range(3):
        A[i][j].append(int(input("Enter element: ")))
        
print("Enter element in B matrix")
B = [3][3]
for i in range(3):
    for j in range(3):
        B[i][j].append(int(input("Enter element: ")))
        
sum =[3][3]
for i in range(3):
    for j in range(3):
        sum[i][j].append(A[i][j]+B[i][j])
        
print("Sum of matrix A and B is : ")
for i in range(3):
    for j in range(3):
        print(sum[i][j], end="\t")
    print("\n")


