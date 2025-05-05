x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
t = [1, -1, -1, -1]  # Target output (for AND gate)

w1 = int(input("Enter the weight1: "))
w2 = int(input("Enter the weight2: "))
a = int(input("Enter the learning rate: "))
b = int(input("Enter the bias: "))
threshold = 0.2

print("itr\tx1\tx2\tt\tyin\ty\tw1\tw2\tb")
for j in range(len(x1)*3):
    i = j%(len(x1))
    yin = b + x1[i]*w1 + x2[i]*w2

    if yin > threshold:
        y = 1
    elif yin < -threshold:
        y = -1
    else:
        y = 0  # Optional (used in Adaline, not typical for perceptron)

    if y != t[i]:
        w1 = w1 + a * t[i] * x1[i]
        w2 = w2 + a * t[i] * x2[i]
        b = b + a * t[i]

    print(f"{i}\t{x1[i]}\t{x2[i]}\t{t[i]}\t{yin}\t{y}\t{w1}\t{w2}\t{b}")
