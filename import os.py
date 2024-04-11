import os #importar librerias 
os.system("cls")
#datos
vnombre=input("ingrese su nombre")
vdias=int(input("ingrese dias trabajados"))
vsueldo=float(input("ngrese sueldoq"))
vabono2=0
vtipo=input("tipo de trabajador (f)ijo / (e)ventual ")
#determinar primer bono
if (vdias>7 and vdias<=17):
    vbono1=5000
else:
    vbono1=2500
    #determinar segundo bono 
if vtipo=="f":
    vbono2=10000
#calcular el salario del trabajador
vtotal=(vdias+vsueldo)+vbono1+vbono2
print("===========================")
print("calculo de nomina realizado")
print("===========================")
print("trabajador       :",vnombre)
print("dias trabajado  :",vdias)
print("dueldo diario   :",vsueldo)
print("tipo de empleado:",vtipo)
print("pago a recibir  :",vtotal)
print("===========================")
input("pulse ENTER para continuar...!")