# Kawerin Grieco Lautaro 44.406.777 25/09/2026

catalogo = [
    {"codigo": 101, "producto": "Cafe con leche", "precio": 1500},
    {"codigo": 102, "producto": "Medialuna", "precio": 700},
    {"codigo": 103, "producto": "Sandwich de miga", "precio": 1800},
    {"codigo": 104, "producto": "Agua mineral 500 ml", "precio": 1000},
    {"codigo": 105, "producto": "Empanada", "precio": 1200},
    {"codigo": 106, "producto": "Chipa (100 g)", "precio": 1300}
]

ventas_dia=[]
ventas_semana=[]
dias=["NoName","Lunes","Martes","Miercoles","Jueves","Viernes"]

def convertir_dia (num):
    if 0<num<6
        return dias[num]
    
i=1 # Con tal de respetar la numeracion que se le da a los dias de la semana, se comienza en 1
while i in range(6):
    print(convertir_dia(i))
    carga=(input("Si desea cargar una venta, ingrese 1. Si desea cerrar el programa por el dia, ingrese 2: "))
    if carga == 1:
        print(catalogo)
        dia_venta=i
        cod_id=int(input("Ingrese el codigo del producto vendido: "))
        cant_product=int(input("Ingrese la cantidad de dicho producto: "))
        ventas_dia.append({"dia": dia_venta, "cod": cod_id, "cantidad": cant_product})
    else:
        


