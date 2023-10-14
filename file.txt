# Multiplication table
def mul (n):
    for i in range(1,11):
        print(n,"*",i," = ", n*i)
n = int(input("Enter n: "))
mul(n)