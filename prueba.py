import pytest
from funciones_tp5 import *

#8.	Diseñar una función que calcule el área y el perímetro de una circunferencia.
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia
# y muestre su área y perímetro.


@pytest.mark.parametrize("username, password, intentos, res",[("usuario1","sfss",1,(False,2)),("dasjd","asdasd",2,(False,3)),("usuario1","asdasd",0,(True,1))])
def test_login(username, password, intentos, res):
    assert(username, password, intentos) == res

