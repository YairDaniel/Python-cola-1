
# validar si la cola esta vacia 
if frente == final:
    print("la cola esta vacia.")
    exit(1)
#Obtener un elemento de la cola 
primerElemento = A[(frente + 1)% MaxTamC]
print("El primer elemento de la cola es:{primerElemento")
#Eliminar un elemento de la cola
frente = (frente + 1)% MaxTamC

#Imprimir elementos de la cola en el orden en que fueron ingresados 
print("Elementos de la cola en el orden de ingreso:")
i = (frente + 1)% MaxTamC
while i !=(final + 1)% MaxTamC:
    print(A[i], end="")
    i = (i + 1)% MaxTamC
    print()