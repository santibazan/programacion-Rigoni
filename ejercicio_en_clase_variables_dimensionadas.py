#1. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
#forma: (nombre, dni, destino). Por ejemplo:
#*(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+
#Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
#*(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+
#Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
#   - Agregar pasajeros a la lista de viajeros.
#   - Agregar ciudades a la lista de ciudades.
#   - Dado el DNI de un pasajero, ver a qué ciudad viaja.
#   - Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#   - Dado el DNI de un pasajero, ver a qué país viaja.
#   - Dado un país, mostrar cuántos pasajeros viajan a ese país.
#   - Salir del programa

lista_pasajeros = []
lista_ciudades = []

while True:
    print("Ingrese 1 para agregar pasajeros a la lista")
    print("Ingrese 2 para agregar ciudades a la lista")
    print("Ingrese 3 para ingresar el dni de la persona para ver a que ciudad viaja")
    print("Ingrese 4 para mostrar la cantidad de pasajeros que van a tal ciudad")
    print("Ingrese 5 para ingresar el dni de la persona para ver a que pais viaja")
    print("Ingrese 6 para mostrar la cantidad de pasajeros que van a tal pais")
    print("Ingrese 7 para salir del programa")

    option = int(input("Ingrese la opcion deseada: "))

    if option == 1:
        name = str(input("Ingrese el nombre de la persona: "))
        dni = int(input("Ingrese el DNI de la persona: "))
        destino = str(input("Ingrese el destino del pasajero: "))
        lista_pasajeros.append(name, dni, destino)
        
    elif option == 2:
        ciudad = str(input("Agrege ciudades: "))
        pais = str(input("Ingrese el pais de la ciudad: "))
        lista_ciudades.append(ciudad, pais)

    elif option == 3:
        dni = int(input("Ingrese el DNI del pasajero: "))
        found = False
        for pasajero in lista_pasajeros:
            if pasajero[1] == dni:
                destiny_city = pasajero[2]
                found = True
                break
        if (found):
            print(f"El pasajero viaja a {destiny_city}")
        else:
            print("DNI no encontrado")

    elif option == 4:
        city = str(input("Ingrese la ciudad para ver cuantas personas viajan ahi: "))
        city = city.lower()
        counter = 0
        for i in lista_pasajeros:
            if (i[2]==city):
                counter=counter+1
        print(f"La cantidad de viajeros que van a {city} son {counter}")

    elif option == 5:
        dni = int(input("Ingrese el DNI de la persona para ver a que pais viaja: "))
        found = False
        for pasajero in lista_ciudades:
            if pasajero[1] == dni:
                destiny_pais = pasajero[2]
                found = True
                break
        if (found):
            for city, pais in lista_ciudades:
                if city == destiny_city:
                    print(f"El pasajero va a viajar a {pais}")
                    break
    
        else:
            print("DNI no encontrado")

    elif option == 6:
        pais = str(input("Ingrese pais para ver cuantas personas viajan ahi: "))
        pais = pais.lower()
        counter = 0
        for i in lista_ciudades:
            if (i[1]==pais):
                counter=counter+1
            else:
                pass
        print(f"La cantidad de viajeros que van a {pais} son {counter}")

    elif option == 7:
        print("Saliendo del programa")
        break
    else:
        print("Ingrese una opcion valida: ")



