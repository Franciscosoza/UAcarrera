#usos de librerias
os.system("cls")  # borra la plantilla
#entrada de datos
vrut=input("ingrese rut")
vnombre=input("ingrese su nombre").upper() # PERMITE COMBERTIR A MAYUSCULAS 
vdireccion=input("su direccion").upper() # PERMITE COMBERTIR A MAYUSCULAS
vcorreo=input("ingrese su correo").lower() #convierte a minusculas 
vedad=int(input("su edad"))
vsueldo=float(input("su sueldo"))
vdias=int(input("dias trabajados"))
#proceso
vtotal=vdias*vsueldo
#salida
print("=== DATOS DE LA NOMINA ===")
print("==========================")
print("RUT:",vrut)
print("SUELDO:",vsueldo)
print("Dias que trabaja",vdias) 
print("total a cobrar:",vtotal)
