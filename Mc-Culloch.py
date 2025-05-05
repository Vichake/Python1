# Inputs for AND and OR
x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
t_and = [1, -1, -1, -1]
t_or = [1, 1, 1, -1]
t_xor = [-1,1,1,-1]
t_xnor = [1,-1,-1,1]

# Inputs for NOT
x_not = [1, -1]
t_not = [-1, 1]

# Gate Selection
print("Select a logic gate:")
print("1. AND")
print("2. OR")
print("3. NOT")
choice = int(input("Enter your choice (1/2/3): "))

# Input selection
if choice == 3:
    # Unary NOT operation
    w = int(input("Enter the weight: "))
    O = int(input("Enter the threshold: "))
    b = int(input("Enter the bias: "))
    a = 1  # Learning rate

    print("\nTruth Table (NOT):")
    print(" Input Output Expected")
    for i in range(len(x_not)):
        yi = x_not[i] * w + b
        y = 1 if yi >= O else -1
        print(f" {x_not[i]:<6} {y:<6} {t_not[i]:<6}")

        if y == t_not[i]:
            print("  Matched!")
        else:
            print("  Not Matched! Updating weight...")
            w = w + a * t_not[i] * x_not[i]
            b = b + a * t_not[i]
            print(f"  Updated Weight: w={w}, bias={b}\n")

    print(f"\nFinal Weight: w={w}, bias={b}")
else:
    if(choice == 1):
        t = t_and
    else:
        t = t_or
    w1 = int(input("Enter the weight 1: "))
    w2 = int(input("Enter the weight 2: "))
    O = int(input("Enter the threshold: "))
    b = int(input("Enter the bias: "))
    a = 1  # Learning rate

    print("Truth table")
    print("Input1 Input2 Expected Output ")
    for i in range(len(t)):
        yi = x1[i]*w1 + x2[i]*w2 + b
        if yi >= O:
            y = 1
        else:
            y=-1
        print(f"{x1[i]:<6}{x2[i]:<6}{t[i]:<6}{y:<6}")

        if y==t[i]:
            print()
        else:
            w1 = w1+ a*x1[i]*t[i]
            w2 = w2+ a*x2[i]*t[i]
            b = b+a*t[i]

