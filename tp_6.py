# 1. Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
#Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.

nums = []

while True:
    n = int(input("Ingrese numeros para guardarlos en una lista, para finalizar marque 0: "))
    if n != 0: 
        nums.append(n)
    else:
        break

print(nums)

#2.A continuación, solicitar al usuario que ingrese un número y, si el número está en la
#lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

number = int(input("Ingrese un numero para buscarlo en dicha lista y eliminarlo: "))
if number in nums:
    nums.remove(number)
    print(f"{number} ha sido eliminado de la lista.")
else:
    print(f"{number} no está en la lista.")
print(nums)

#3.Imprimir la sumatoria de todos los números de la lista.
summary = 0
for i in range(len(nums)):
    summary = summary + nums[i]

print(f"La suma de todos los elementos de la lista es {summary}")

#4.Solicitar al usuario otro número y crear una lista con los elementos de la lista 
# original, que sean menores que el número dado. Imprimir esta nueva lista, iterando 
# por ella.

list_length = 5

number = int(input("Ingrese un numero para crear una lista con numeros menores a este: "))
minor_numbers_list = [random.randint(1,number-1) for _ in range(list_length)]

for i in range(len(minor_numbers_list)):
    print(minor_numbers_list[i])
    
deletor = int(input("Ingrese otro numero: "))
for i in range(len(nums)):
    if nums[i] > number:
        nums[i]=deletor
    else:
        break
print(f"La nueva lista quedara asi: {nums}")
