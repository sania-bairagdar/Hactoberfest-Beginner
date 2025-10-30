a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
choice = int(input("Choose: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
else:
    print("Invalid choice")
