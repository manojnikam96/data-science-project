num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 21):
    print(num, "x", i, "=", num * i)
    num = int(input("Enter a number: "))
    print("Multiplication Table of", num)
