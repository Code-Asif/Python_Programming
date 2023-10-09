#Python program to find the Nth term in a Fibonacci series using recursion

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(fib(i), end="\t")


