import funciones

#ejercicio en clase 1
num = int(input("Numeros a procesar:  "))

while(num!=0):
    print(f"suma : {funciones.function(num)}")
    num = int(input("Numeros a procesar:  "))

#ejercicio de funciones
x=int(input("Un numero: "))
y=int(input("Otro numero: "))

print(funciones.most(x-3, funciones.least(x+2, y-5)))