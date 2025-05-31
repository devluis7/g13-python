#Entrada
tabla = int(input("Ingrese la tabla de multiplicar que desea mostrar: "))
valor1 = tabla * 1
valor2 = tabla * 2
valor3 = tabla * 3
#Salida
print(str(tabla)+ "X 1 = " + str(valor1))
print(str(tabla)+ "X 2 = " + str(valor2))
print(str(tabla)+ "X 3 = " + str(valor3))
#Tabla de multiplicar usando For
contador = 1
print("Tabla usando For")
for contador in range(1,13,1):
    valor = tabla *  contador
    print(str(tabla) + ' X ' + str(contador) + ' = ' + str(valor))