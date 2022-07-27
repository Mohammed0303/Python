def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

print("Enter your choice (a,b,c,d)")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.division")

choice = input("\n""Enter your choice here: ")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if choice == 'a':
    print("The sum of", num1, "+", num2, "=", add(num1, num2))
elif choice == 'b':
    print("The difference of", num1, "-", num2, "=", sub(num1, num2))
elif choice == 'c':
    print("The product of", num1, "*", num2, "=", mul(num1, num2))
elif choice == 'd':
    print("The divisor of", num1, "/", num2, "=", div(num1, num2))
else:
    print("You have entered wrong choice. Try again. Thank You!!!")

