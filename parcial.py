loop = 1
#Aca le pedimos al usuario que ingrese su nombre.
name=str(input("Bienvenido, Ingrese su nombre: "))

#Aca le pedimos al usuario que ingrese una opcion para jugar
while loop==1:

    game=int(input(f"{name}, por favor ingrese 1 para el juego de numero o 2 para el juego de palabras: "))

    number_entire = 1
    largest_pear=0
    average=0
    contador_impar=0
    sumaImpares=0
    #validamos el juego que quiera jugar el usuario
    if game==1:
        while number_entire!=0:
            #Aca le pedimos que ingrese un numero entero
            number_entire=int(input(f"{name}, por favor ingrese un numero entero: "))
            if number_entire%2==0:
                if number_entire>largest_pear:
                    largest_pear=number_entire

            elif number_entire%2!=0:  
                contador_impar+=1
                sumaImpares= sumaImpares+number_entire
            else:
                break
        average=sumaImpares/contador_impar    
        #Imprimimos el numero par mayor
        print(f"{name}, el mayor numero par es: {largest_pear}")  
        #imprimimos el promedio de los numeros impares  
        print(f"{name}, el promedio de los numeros impares es: {average}")
    
        loop=int(input(f"{name}, si queres jugar a otro juego, pulsa 1, si queres salir pulsa 2: "))

    elif game==2:

        contadorA=0
        contadorE=0
        contadorI=0
        contadorO=0
        contadorU=0
        #Aca le pedimos al usuario que ingrese una frase para saber la cantidad de vocales que contiene dicha frase
        phrase=str(input(f"{name}, ingrese una frase: ")).upper()
        
        for i in range(len(phrase)):
            if phrase[i] == "A":
                contadorA= contadorA + 1
            elif phrase[i] == "E":
                contadorE= contadorE + 1        
            elif phrase[i] == "I":
                contadorI= contadorI + 1  
            elif phrase[i] == "O":
                contadorO= contadorO + 1  
            elif phrase[i] == "U":
                contadorU= contadorO + 1          
            
        #Imprimimos la cantidad de vocales de cada una    
        print(f"{name}, hay {contadorA} vocal A")
        print(f"{name}, hay {contadorE} vocal E")
        print(f"{name}, hay {contadorI} vocal I")
        print(f"{name}, hay {contadorO} vocal O")
        print(f"{name}, hay {contadorU} vocal U")

        loop=int(input(f"{name}, si queres jugar a otro juego, pulsa 1, si queres salir pulsa 2: "))
print(f"gracias por jugar {name}")