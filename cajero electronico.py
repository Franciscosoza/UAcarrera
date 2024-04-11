#importamos las librerias 
import os 

Rb1deposito=0
Rb2retirodinero=0
Rb3md=0
rb4changekey=0
while Rb1deposito == 0:
    os.system("Cls")

    #menu - atm
    print("1.->deposito de dinero")
    print("2.->retiro de dinero")
    print("3.->mostrar saldo de cuenta")
    print("4.->cambio de clave")
    print("5.->salir")

    #pedimos la opcion al usuario
    vop= int(input("su opcion: "))

    #procesamos la opcion 
    if vop == 1:
        
        #cuanto quiere depositar 
        vcantidad = int(input("cuanto quiere depositar:"))
        
        #mostramos un mensaje de confirmacion 
        input("deposito realizado con exito,pulse ENTER")
    
    elif vop == 2: 
        #cuanto quiere retirar
        vcantidad = int(input("cuanto dinero quiere retirar"))

        #mostramos un mensaje de confirmacion
        input("retiro realizado con exito,pulse ENTER")

    elif vop == 3:  
        #saldo total de la cuenta 
        vcantidad = int(input("saldo mostrado:")) 
    
        #muestranos un mensaje de confirmacion 
        input("saldo mostrado con exito,pulse ENTER")

     
            