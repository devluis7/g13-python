#while (condicion)
opcion = 0
opcion = input("ingrese opcion: ")
while (opcion == "0"):
    print("=========================== Opciones ===========================")
    print(" 1) Opción 01")
    print(" 2) Opción 02")
    print(" 3) Opción 03")
    print(" 4) Salir")
    
    opcion = int(input("Opcion elegida: "))
    print ("Ud. seleccionó la opción: " + str(opcion))
    salir = input ("Desea salir (Si/No)")
    if (salir == "no"):
        opcion = 0
    
          