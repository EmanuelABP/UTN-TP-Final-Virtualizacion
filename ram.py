#Se crea una lista
ram_dispositivo=[]

#Pedimos la ram total del dispositivo
ram_total=int(input("Cuanta memoria RAM tiene tu PC en GB? "))
ram_dispositivo.append(ram_total)

#Pedimos la ram asignada a la maquina virtual VM
ram_vm=int(input("Cuanta memoria RAM le asignaste a la VM en GB? "))
ram_dispositivo.append(ram_vm)

#Calcular la RAM disponible
ram_disponible=ram_dispositivo[0]-ram_dispositivo[1]
ram_dispositivo.append(ram_disponible)

#Mostrar por pantalla el resimen de los valores
print ("\nResumen del uso de memoria RAM: ")
print (f"- RAM total de la PC: {ram_dispositivo[0]} GB")
print (f"- RAM asignada a la maquina virtual: {ram_dispositivo[1]} GB")
print (f"- RAM disponible restante: {ram_dispositivo[2]} GB")