import os # importando la libreria del S.O
os.system("cls") # limpiando la plantilla 
#paso 1: LEER LOS DATOS
print("===========================================")
vnombre= input("Nombre del Estudiante ")
vnota1=float(input("ingrese la nota"))
vnota2=float(input("ingrese la nota"))
vnota3=float(input("ingrese la nota"))
#paso 2: PROCESO
vpromedio=(vnota1+vnota2+vnota3)/3
if vpromedio>=4:
     print("EL ALUMNO:", vnombre)
     print("obtuvo su promedio de:",vpromedio)     
     print("su estatus es : APROBADO")
else:
     print("EL Alumno:" ,vnombre," su nota final fue:",vpromedio)
     print("estatus:REPROBADO")
print("PROGRAMA FINALIZADO EXITOSAMENTE")
print("PUSE [ENTER] PARA CONTINUAR..!")