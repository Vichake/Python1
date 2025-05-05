# Delta Rule (Adaline) Implementation for AND gate

x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
t = [1, -1, -1, -1]  # Target for AND gate

# Initial values
w1 = float(input("Enter initial weight w1: "))
w2 = float(input("Enter initial weight w2: "))
b = float(input("Enter initial bias: "))
eta = float(input("Enter learning rate (e.g., 0.1): "))
epochs = int(input("Enter number of epochs: "))

print("\nEpoch\tSample\tX1\tX2\tYin\tTarget\tError\tUpdated w1\tUpdated w2\tUpdated Bias")
print("------------------------------------------------------------------------------------------")

for epoch in range(epochs):
    print(f"Epoch {epoch + 1}")
    for i in range(len(x1)):
        yin = w1 * x1[i] + w2 * x2[i] + b
        error = t[i] - yin

        # Update weights and bias
        w1 = w1 + eta * error * x1[i]
        w2 = w2 + eta * error * x2[i]
        b = b + eta * error

        print(f"\t{i + 1}\t{x1[i]}\t{x2[i]}\t{yin:.2f}\t{t[i]}\t{error:.2f}\t{w1:.2f}\t\t{w2:.2f}\t\t{b:.2f}")
    print("------------------------------------------------------------------------------------------")

print("\nFinal weights and bias:")
print(f"w1 = {w1:.2f}, w2 = {w2:.2f}, bias = {b:.2f}")
