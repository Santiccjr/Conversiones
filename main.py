import math

opc = 0
while(opc != 3):
 print('=================MENU=============')
 print('1) Polares a Cartesiana')
 print('2) Cartesiana a Polares')
 print('3) Salir')
 opc = int(input('-> '))
 
 if (opc == 1):
    angle = float(input("Ingresa el angulo: "))
    radio = float(input("Ingresa el radio: "))
    
    angulo = math.radians(angle)
    x = radio*math.acos(angulo)
    y = radio*math.asin(angulo)
    
    print(f'Tus cordenadas son ({x},{y})')

   


