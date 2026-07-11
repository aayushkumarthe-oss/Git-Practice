a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

a, b = b, a
c, d = d, c

print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
