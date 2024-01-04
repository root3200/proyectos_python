import json
import random
from datetime import datetime

n1 = datetime.now()
print(n1.strftime("%Y-%m-%d %H:%M"))


#AGENDA TELEFONICA 
##UBICACIO DEL ARCHIVO JSON
path ="/home/r4m3200/Escritorio/python_ejercicios/Agenda_telefonica_v3/data.json"

print("[!] - EDITAR USUARIO\n")
usuario = input("ID usuario: ")

with open(path, "r") as f:
    f_data = json.load(f)
    busqueda = usuario
    existe = False
    for index, i in enumerate(f_data):
        if busqueda == i['id']:
            print(f"Usuaruaio {i['id']} econtrado \n\n\tNombre: {i['nombre']} \n\tApellido: {i['apellido']} \n\tInformacion: \n\t\tEdad: {i['informacion']['edad']} \n\t\tSexo: {i['informacion']['sexo']} \n\t\tDireccion: {i['informacion']['direccion']} \n\t\tTrabajo: {i['informacion']['trabajo']}")
            
            existe = True
            break
    if not existe:
        print(f"[!] - El usuario {busqueda} no existe")
print(index)
opcion = input("Editar usuario \n1-nombre\n2-apelldio\n3-direccion\n4-trabajo\n:> ")

if opcion == "1":
    with open(path, 'r') as f:
        f_data = json.load(f)
        
        while True:
            cambio = input("nuevo nombre")
            f_data[index]['nombre'] = cambio
            if cambio:
                break
            else:
                print("[!] - No puedes dejar el campo vacio")
    with open(path, 'w') as f:
        json.dump(f_data , f, indent=2) 
                