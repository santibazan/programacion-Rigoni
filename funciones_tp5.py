import math
#Ejercicio 1
def DNI(dni):
    return len(dni)==7 or len(dni)==8
#Ejercicio 2

def long_last_word(phrase):
    long = phrase.split()
    last_word = long[-1]
    length_word =len(last_word)
    return length_word


#Ejercicio 4

def multiplo(a,b):
    if(a%b==0):
        return True
    elif (a%b==0):
        return True
    else:
        return False
        
#Ejercicio 5
def temperature(min, max):

    med= (min + max) / 2
    return med

#Ejercicio 6
def frase(phrase):
    phrase=" ".join(phrase)
    return phrase

#Ejercicio 7


#Ejercicio 8
def circle(radio):
    area=(radio*radio)* 3.14
    perimetro=(2*3.14)*radio
    return area, perimetro

#Ejercicio 9
def login(u,p):
    if (u == "usuario1" and p == "asdasd"):
        return True
    else:
        return False

#Ejercicio 10
def discount(prize, discountt):
    final_prize = prize * (1 - discountt / 100)
    return final_prize

#ejercicio 11
def modified_list(listt):
    for i in range(len(listt)):
        listt[i] += 1

def list_new(listtt):
    modified_list(listtt)
    return listtt

#Ejercicio 12
def lenght_dictionarie(phrase):
    phrase = phrase.split()
    words_dictionarie = {}
    for i in phrase:
        words_dictionarie[i] = len(i)

    return words_dictionarie

#Ejercicio 13
def vector(vector1, vector2):
    modulo=math.sqrt((vector1**2)+(vector2**2))
    return modulo

#ejrcicio_14

def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#ejercicio_15
def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

#ejercicio_16
def appareances(num,num_to_find,c):
    num=str(num)
    
    for i in range(len(num)):
        if (num[i]==num_to_find):
            c= c + 1
    return c

    
        