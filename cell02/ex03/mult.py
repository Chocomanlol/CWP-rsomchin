num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

product = num1 * num2

print(f"{num1} x {num2} = {product}")

if product > 0:
    print("The result is positive.")
elif product < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")