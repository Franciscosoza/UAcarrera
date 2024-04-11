#marra
        vtotal = vtotal + (vcantidad * 0.5)

        # Mostramos un mensaje de confirmación
        input("Venta realizada con éxito, pulse ENTER")

    elif vopcion == 2:
        # Pedimos la cantidad de ayuyas
        vcantidad = int(input("Cuantas ayuyas: "))

        # Actualizamos el total
        vtotal = vtotal + (vcantidad * 1.0)

        # Mostramos un mensaje de confirmación
        input("Venta realizada con éxito, pulse ENTER")

    elif vopcion == 3:
        # Pedimos la cantidad de sopaipillas
        vcantidad = int(input("Cuantas sopaipillas: "))

        # Actualizamos el total
        vtotal = vtotal + (vcantidad * 1.5)

        # Mostramos un mensaje de confirmación
        input("Venta realizada con éxito, pulse ENTER")

    elif vopcion == 4:
        # Mostramos la totalización
        print()
        print("*** TOTALIZACIÓN ***")
        print("Total marraquetas:", vconsarra)
        print("Monto de ventas:", vconsarra * 0.5)
        print("Total ayuyas:", vcontayuya)
        print("Monto de ventas:", vcontayuya * 1.0)
        print("Total sopaipillas:", vcontsopaipa)
        print("Monto de ventas:", vcontsopaipa * 1.5)
        print("Total:", vtotal)

        # Salimos del bucle
        vcontinuar = "n"

    else:
        # Mostramos un mensaje de error
        print("Opción no válida")