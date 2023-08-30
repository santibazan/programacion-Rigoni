#1-	Crear un programa que reciba el número de años que tiene nuestra computadora y
#muestre en la consola que el computador es nuevo si es menor o igual a 2 años y 
#que el computador es viejo si es mayor a 2 años.
condicion=int(input("Ingrese los años de su computadora: "))
if(condicion<=2):
    print("La computadora es nueva")
else:
    print("La computadora es vieja")    

#2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita
#un número negativo.
condicion1=int(input("Ingrese los años de su computadora: "))
if(condicion1>2):
    print("La computadora es vieja")
elif(condicion1>0 and condicion1<=2):
    print("La computadora es nueva") 
else:
    print("numero invalido")    

#3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se
# almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos
# nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.

nombre1=input("ingrese el primer nombre: ")
nombre2=input("ingrese el sugundo nombre: ")
if(nombre1[0] == nombre2[0]):
    print("Hay coincidencia")
else:
    print("No hay coincidencia")


#4-	Crear un programa que permita al usuario elegir un candidato por el cual votar.
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido
# verdad, candidato C por el partido azul.
print("Ingrese 1 para votar al candidato A del partido rojo")
print("Ingrese 2 para votar al candidato B del partido verde")
print("Ingrese 3 para votar al candidato C del partido azul")
candidato=int(input())
if(candidato==1):
    print("usted voto al candidato A del partido rojo")
elif(candidato==2):
    print("usted voto al candidato B del partido verde")
elif(candidato==3):
    print("usted voto al candidato C del partido azul")
else:
    print("Voto invalido")   

#5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar 
# el mensaje ‘Es vocal’.
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más
# de un carácter, informarle que no se puede procesar el dato.

letra=input("ingrese una letra: ")
letra=letra.lower()
if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"):
    print("Es vocal")
else:
    print("no es vocal")    

#6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea 
# bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que
#  también sea divisible por 400.
anio=int(input("Ingrese un año para saber si es biciesto o no: "))
if(anio%4==0 and anio%100!=0):
    print("Es biciesto")
elif(anio%100==0 and anio%400==0):
    print("Es biciesto")
else:
    print("No es biciesto")    

#7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla
# al menor de los tres.

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

if(num1<num2 and num1<num3):
    num_menor=num1
elif(num1<num2 and num1>num3):
    num_menor=num3
else:
    num_menor=num2        
print(f"el numero menor es {num_menor}")

#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
#  Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla 
# “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña 
# no coinciden, mostrar “Acceso denegado”.

usuario=input("Ingrese el usuario: ")
contrasenia=input("Ingrese la contraseña: ")

if(usuario=="Gwenevere" and contrasenia=="excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")    

#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo 
# y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
#  pantalla el grupo que le corresponde.
nombre=input("ingrese su nombre: ")
sexo=input("ingrese su sexo: ")

nombre=nombre.lower()
sexo=sexo.lower()

if(nombre[0]<"m" and sexo=="f" or nombre[0]>"n" and sexo=="m"):
    print("pertenece al grupo A")
else:
    print("pertenece al grupo B")

#10-Escribir un programa para una empresa que tiene salas de juegos para todas las
# edades y quiere calcular de forma automática el precio que debe cobrar a sus 
# clientes por entrar. El programa debe preguntar al usuario la edad del cliente 
# y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar 
# gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad=int(input("Ingrese su edad: "))
if(edad<4):
    print("Entrada gratis")
elif(edad>4 and edad<18):
    print("Entrada de U$D500")    
else:
    print("Entrada de U$D1000")

#11-La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus #clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza=int(input("Ingrese 1 para elejir la pizza vegetariana o 2 para pizza no vegetariana: " ))

if(pizza==1):
    print("Usted elijio la pizza vegetariana")
    ingred_veg=int(input("Presione 1 para elejir pimiento o 2 para tofu: "))
    if(ingred_veg==1):
        print("Su pizza contiene muzzarella, salsa de tomate y pimienta")
    elif(ingred_veg==2):
        print("Su pizza contiene muzzarella, salsa de tomate y tofu")
    else:
        print("Ingrediente invalido")
elif(pizza==2):
    print("Usted elijio la pizza con carne")       
    ingred_car=int(input("Presione 1 para elejir peperoni, 2 para jamon o 3 para salmon: ")) 
    if(ingred_car==1):
        print("Su pizza contiene muzzarella, salsa de tomate y peperoni")
    elif(ingred_car==2):
        print("Su pizza contiene muzzarella, salsa de tomate y jamon")
    elif(ingred_car==3):
        print("Su pizza contiene muzzarella, salsa de tomate y salmon")    
    else:
        print("Ingrediente invalido")
else:
    print("Pizza invalida")        

#12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

anio_actual=int(input("Ingrese el año actual: "))
anio_cualq=int(input("Ingrese un año cualquiera: "))
if(anio_actual>anio_cualq):
    dif=anio_actual-anio_cualq
    print(f"Han pasado {dif} años del {anio_cualq}")
else:
    dif=anio_cualq-anio_actual
    print(f"Faltan {dif} años para el {anio_cualq}")

#13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))

if(num1>num2):
    if(num1%num2==0):
        print(f"El {num1} es multiplo del {num2}")   
elif(num2>num1):
    if(num2%num1==0):
        print(f"El {num2} es multiplo del {num1}")        
else:
    print("Valores invalidos")

#14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a
a = float(input("Ingrese el coeficiente de la ecuacion de primer grado: "))
b = float(input("Ingrese el termino independiente de la ecuacion de primer grado: "))
if (a == 0 and b == 0):
    print("La ecuacion tiene infinitas soluciones")
elif (a == 0 and b != 0):
    print("La ecuacion no tiene solucion")
else:
    print(f"La solucion de la ecuacion es {-b / a}")

#15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
import math
preg=input("Ingrese T para calcular el area de un triangulo, o C para la de un circulo: ")

preg=preg.upper()

if(preg=="T"):
    base=int(input("Ingrese la base del triangulo: "))
    altura=int(input("Ingrese la altura del triangulo: "))
    area=(base*altura)/2
    print(f"EL area del triangulo es de {area}")
elif(preg=="C"):
    radio=int(input("Ingrese el radio del circulo: "))
    area=math.pi*radio**2
else:
    print("Figure not found")    

#16-	Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#•	Si operación es 1 entonces debemos ver el resultado de a + b
#•	Si operación es 2 entonces debemos ver el resultado de a * b
#•	Si operación es 3 entonces debemos ver el resultado de a - b
#•	Si operación es 4 entonces debemos ver el resultado de a / b

val1=int(input("Ingrese el primer numero para operar: "))
val2=int(input("Ingrese el segundo numero para operar: "))

oper=int(input("Ingrese 1 para sumar, 2 para multiplicar, 3 para restar o 4 para dividir"))

if(oper==1):
    suma=val1+val2
    print(f"El resultado de la suma entre {val1} y {val2} es {suma}")
elif(oper==2):
    mult=val1+val2
    print(f"El resultado de la multiplicacion entre {val1} y {val2} es {mult}")
elif(oper==3):
    resta=val1+val2
    print(f"El resultado de la resta entre {val1} y {val2} es {resta}")
elif(oper==4):
    div=val1+val2
    print(f"El resultado de la division entre {val1} y {val2} es {div}")   
else:
    print("operacion invalida")        

#17- Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje. 

dia=input("Ingrese un dia de la semana: ")
dia=dia.lower()

if(dia=="lunes"):
    print("es lunes")
elif(dia=="viernes"):
    print("es viernes")    
elif(dia=="sabado"):
    print("es sabado")
elif(dia=="domingo"):
    print("es domingo")
else:
    print("No coincidieron los dias")        

#18-Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.

horas_t=int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salario=int(input("Ingrese el salario por horas: "))
if(horas_t>45):
    horas_e=horas_t-45
    print(f"Usted trabajo {horas_e} horas extras")
    horas_ex=horas_e*(salario*1.1)
    salario_tot=horas_t*salario+horas_ex
    print(f"Su salario total es de {salario_tot}")
else:
    salario_tot=horas_t*salario
    print(f"Su salario total es de {salario_tot}")    

#19-Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.

lap=int(input("Ingrese la cantidad de lapices que llevara: "))
sub_total=lap*60
if(sub_total>=1000):
    total=sub_total*0.93
    print(f"Usted accedio al descuento del 7% y pagara {total}")
else:
    print(f"Usted no accedio al descuento del 7% y pagara {sub_total}")

#20-Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

nota1=int(input("Ingrese la primer nota: "))
nota2=int(input("Ingrese la segunda nota: "))
nota3=int(input("Ingrese la tercer nota: "))
nota4=int(input("Ingrese la cuarta nota: "))

prom=(nota1+nota2+nota3+nota4)/4

if(prom>=6):
    print("APROBADO")
else:
    print("DESAPROBADO")    