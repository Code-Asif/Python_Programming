#Python program to implement a calculator to do basic operations.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a, "-", b, "=", sub(a, b))

        elif choice == '3':
            print(a, "*", b, "=", mul(a, b))

        elif choice == '4':
            print(a, "/", b, "=", div(a, b))
        break
    else:
        print("Invalid Input")
