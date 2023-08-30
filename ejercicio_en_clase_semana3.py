fecha=input("ingrese la fecha en formato dia, DD/MM: ")
dia=fecha[0:fecha.find(",")]
DD=fecha[fecha.find(" ")+1:fecha.find("/")]
MM=fecha[fecha.find("/")+1:]

dia=dia.lower()
DD=int(DD)
MM=int(MM)

if (dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes"): 
    print("Dia de la semana invalido")
elif(DD<1 or DD>31 or MM<1 or MM>12):
    print("Fecha invalida")
else:
    if(dia=="lunes" or dia=="martes" or dia=="miercoles"):
        examen=input("ingrese si hubo examen o no: ")
        examen=examen.lower()
        if (examen=="si"):
            print("Hubo examen")
            alumnos_aprobados=int(input("ingrese la cantidad de alumnos aprobados: "))
            alumnos_desaprobados=int(input("ingrese la cantidad de alumnos desaprobados: "))
            promedio=(alumnos_aprobados/(alumnos_aprobados+alumnos_desaprobados))*100
            print(f"El promedio es {promedio}")
        else:
            print("No huvo examen")   
    else:
        if(dia=="jueves"):
            porcentaje=int(input("Ingrese el porcentaje de asistencia a clase: "))
            if(porcentaje>50):
                print("Asistio la mayoria")
            else:
                print("No asistio la mayoria")
        elif((DD==1 and MM==1) or (DD==1 and MM==7)):
            print("comienzo de un nuevo ciclo")
            alumnos_nuevos=int(input("Ingrese la cantidad de alumnos nuevos: "))
            arancel=int(input("Ingrese el arancel en $ por cada alumno"))
            ingreso_total=alumnos_nuevos*arancel
            print(f"el ingreso total es de {ingreso_total}")
        else:
            pass
