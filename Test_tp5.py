import pytest
from funciones_tp5 import *

#1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido
# y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
@pytest.mark.parametrize("dni, res",[("44308927", True), ("443089", False), ("4430892", True)] )
def test_DNI(dni, res):
    assert DNI(dni) == res

#2.	Escribir una función que, dado un string, retorne la longitud de la última palabra.
# Se considera que las palabras están separadas por uno o más espacios. También podría
# haber espacios al principio o al final del string pasado por parámetro.
@pytest.mark.parametrize("phrase, res",[("hola soy santiago", 8), ("Me encanta programar", 9)])
def test_long_last_word(phrase, res):
    assert long_last_word(phrase) == res

#4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos
# es múltiplo del otro. Crea una función que reciba los dos números, y devuelve si el 
# primero es múltiplo del segundo.
@pytest.mark.parametrize("a, b, res",[(10, 5, True), (20, 10, True),(11, 2, False)])
def test_multiplo(a, b, res):
    assert multiplo(a, b) == res

#5.	Crear una función que calcule la temperatura media de un día a partir de la
#temperatura máxima y mínima. Crear un programa principal, que utilizando la función
#anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando 
#la media. El programa pedirá el número de días que se van a introducir.
@pytest.mark.parametrize("min, max, res", [(10, 20,15.0), (20, 40, 30.0)])
def test_temperature(min, max, res):
    assert temperature(min, max) == res

#6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un 
# espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “
#. Crea un programa principal donde se use dicha función.
@pytest.mark.parametrize("phrase, res", [("Hola", "H o l a"), ("Joaquin", "J o a q u i n")])
def test_frase(phrase, res):
    assert frase(phrase) == res


#7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor
# máximo y el mínimo. Crea un programa que pida números por teclado y muestre el 
# máximo y el mínimo, utilizando la función anterior.
#@pytest.mark.parametrize()

#8.	Diseñar una función que calcule el área y el perímetro de una circunferencia.
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia
# y muestre su área y perímetro.
@pytest.mark.parametrize("radio, res", [(2, (12.56, 12.56)) ])

def test_circle(radio, res):
    assert circle(radio) == res

#9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una 
# contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la 
# contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer
# login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y 
# se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
@pytest.mark.parametrize("username, password, res",[("usuario1","sfss", False),("dasjd","asdasd", False),("usuario1","asdasd", True)])
def test_login(username, password, res):
    assert login(username, password) == res

#10. Escribir una función que aplique un descuento a un precio. Esta función tiene que
# recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar
# los descuentos a los productos del carrito  y devolver el precio final de la compra.
@pytest.mark.parametrize("prize, in_discount, res",
    [(500,50,250), (4500,48,2340)])

def test_discount(prize, in_discount, res):
    assert discount(prize,in_discount) == res

#11
@pytest.mark.parametrize("num_listt, res",
    [([1,2,3,4,5],[2,3,4,5,6]),([30,12,34,65,62],[31,13,35,66,63])])

def test_list_new(num_listt,res):
    assert list_new(num_listt) == res

#12
@pytest.mark.parametrize("phrase,res",
    [("hola que tal", {"hola":4, "que":3, "tal":3}),("buenos dias", {"buenos":6, "dias":4})])

def test_lenght_dictionarie(phrase,res):
    assert lenght_dictionarie(phrase) == res

#13.Escribir una función que calcule el módulo de un vector.
@pytest.mark.parametrize("vector1, vector2, res", [(10, 15, (18.027756377319946))])
def test_vector(vector1, vector2, res):
    assert vector(vector1, vector2) == res

#14.Requerir al usuario que ingrese un número entero e informar si es primo o no, 
# utilizando una función booleana que lo decida.
@pytest.mark.parametrize("num, res", [(5, True), (4, False)])
def test_prime_number(num,res):
    assert prime_number(num) == res

#15. Escribir un programa que pida números al usuario, motrar el factorial de
# cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar
# una o más funciones, según sea necesario.
@pytest.mark.parametrize("num, res", [(3, 6), (4, 24), (2, 2)])
def test_factorial(num, res):
    assert factorial(num) == res

#16.Solicitar al usuario un número entero y luego un dígito. Informar la cantidad 
# de ocurrencias del dígito en el número, utilizando para ello una función que calcule
# la frecuencia.

@pytest.mark.parametrize("num, num_to_find, c, res", [(554675, 5, 3,3 ), (237620984, 2, 2, 2)])
def test_appareances(num, num_to_find, c, res):
    assert appareances(num, num_to_find, c) == res