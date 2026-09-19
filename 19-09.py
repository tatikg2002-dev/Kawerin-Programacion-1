# ¿ Alumnos = ["Juan", "Maria", "Pedro", "Ana", "Luis"] pero yo quiero saber si esos estan o no estan regular ?

# ¿ Que dictamina si un alumno esta o no esta regular ?

# Necesitamos tener las 4 notas alumnos para poder determinar si estan regulares o no.

# Y saber el % de asistencia de cada alumno.

alumnos = { "nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90 }, 
{ "nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60 }, 
{ "nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95 },
{ "nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85 }


def Control(promedio,asisAprob):
    if promedio >= 6 and asisAprob:
        return True
    else:
        return False

def Regularidad(notas,asis):
    goodAsis=False
    suma=sum(notas)
    promedio=suma/4
    if asis >= 75:
        goodAsis=True
    return Control(promedio,goodAsis)

for Estudiante in alumnos:
    estadoReg= Regularidad(Estudiante["notas"],Estudiante["asistencia"])
    if estadoReg:
       print(f"El alumno {Estudiante["nombre"]} esta regular")
    else:
        print(f"El alumno {Estudiante["nombre"]} NO esta regular")
