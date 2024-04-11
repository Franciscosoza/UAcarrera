x = int(input("Dame un número: "))
y = int(input("Dame otro número: "))
z = int(input("Y ahora, uno más: "))

if x == 0 or y == 0 or z == 0:
    print("Al menos uno de los números ingresados es cero.")
elif x < 0 or y < 0 or z < 0:
    print("Al menos uno de los números ingresados es negativo.")
else:
    print("Suma:", x + y + z)
    print("Resta:", x - y - z)
    print("Multiplicación:", z * y * x)
    print("División:", x / y / z)