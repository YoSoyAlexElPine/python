a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    a, b = b, a

sum = 0

while a <= b:
    sum += a
    a += 1
print("La suma de los números entre", a, "y", b, "es", sum)