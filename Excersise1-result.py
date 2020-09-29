listaRegistro = []
nombre = input("Bienvenido al programa que te ayudara a tener la cuenta de tus clientes dentro de tu restaurante. Por favor, ingresa tu nombre: ")
cantidadDeCliente = int(input("ingresa cuantos clientes tuviste, "+nombre+": "))
cliente = 0
total = 0
while cliente <= 10000000000000000000000000000:
    print("Hola, "+ nombre)
    print("ingresa el cliente que visito tu restaurante el dia de hoy ")
    clientes = input("Nombre del cliente: ")
    producto = input("Producto: ")
    costo = float(input("costo ($0.00): "))
    total += costo
    continuar = input("para continuar ingresando mas clientes escriba -si- para parar escriba -no- ")
    registro = {"clientes":clientes, "producto":producto, "costo":costo}
    listaRegistro.append(registro)
    cliente =+ 1
    if continuar == "no":
        break
print("total de clientes con sus nombres: ")    
for registro in listaRegistro:
    print(registro)

print("El costo total es de:")

print(total)

  

  







        
            
    


    

