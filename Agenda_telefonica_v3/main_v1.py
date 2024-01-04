import json
import random
from datetime import datetime
import os

##ARCHIVOS
PATH = "data.json"
PATH2 = "nombre_apellidos_direcciones_oficios.txt"
PATH3 = "log.json"

##VERIFICAR 
def crear_archivos():
    ruta_1 = os.path.join(os.getcwd(), PATH)
    ruta_3 = os.path.join(os.getcwd(), PATH3)

    try:
        with open(PATH, "r") as f:
            f.read()
        with open(PATH3, "r") as f:
            f.read()

    except FileNotFoundError as e:
        if e.strerror == "No such file or directory":
            with open(ruta_1, "x") as f:
                f.write("[\n\n]")
            with open(ruta_3, "x") as f:
                f.write("[\n\n]")

def datos_aleatorios():##NOMBRES ,APELLIDOS, DRIECCIONES, OFICIOS ALEATORIOS

    with open(PATH2, "r", encoding='utf-8',) as f:
        f_data = f.readlines()
        n2= random.choice(f_data)
        n3 = n2.strip().split(',')

        ##ESTRUCTURA DATA JSON
        id_ = random.randint(1000,9999)

        data = {
            "id": f"FG{id_}R",
            "nombre": n3[2],
            "apellido": n3[3],
            #"nombre": f"nombre-{random.randint(1000,9999)}",
            #"apellido": f"apellido-{random.randint(1000,9999)}",
            "informacion": {
                "edad": random.randint(18,60),
                "sexo": "H/M/B",
                "direccion": n3[1],
                "trabajo": n3[0]
                }
            }
        
        ##ESTRUCTURA DATA_LOG JSON
        
        n1 = datetime.now()
        fecha_ = n1.strftime("%Y-%m-%d %H:%M")
        
        data_log = {"ID": f"FG{id_}R", "FECHA": f"{fecha_}"}

        return data,data_log

def agregar_usuario():

    print("Agregar usuario")
    data_log_1, data_log_2 = datos_aleatorios()
    
    ##ABRIR ARCHIVO JSON MODO LECTURA
    with open(PATH, "r") as f:
        f_data = json.load(f)
        f_data.append(data_log_1)
    
    ##ABRIR ARCHIVO JSON MODO ESCRITURA
    with open(PATH, "w") as f:
        json.dump(f_data, f, indent=2)

    
    ##AÑADIR LOG
    
    with open(PATH3, "r") as f_log:
        f_data_log = json.load(f_log)
        f_data_log.append(data_log_2)

    with open(PATH3, "w") as f_log:
        json.dump(f_data_log, f_log, indent=2)
    

def buscar_usuario():
    
    ##ABRIR ARCHIVO JSON MODO LECTURA
    with open(PATH, "r") as f:
        f_data = json.load(f)
        busqueda = input("ID usuario: ")
        existe = False
        #global index
        for index, i in enumerate(f_data):
            if busqueda == i['id']:
                print(f"Usuaruaio {i['id']} econtrado \n\tNombre: {i['nombre']} \n\tApellido: {i['apellido']} \n\tInformacion: \n\t\tEdad: {i['informacion']['edad']} \n\t\tSexo: {i['informacion']['sexo']} \n\t\tDireccion: {i['informacion']['direccion']} \n\t\tTrabajo: {i['informacion']['trabajo']} \n\t\tPos: {index}")
                existe = True
                return index
                break
        print("<<<<<<<<<<<<<<<<<")
        if not existe:
                #print(f"[!] - El usuario {busqueda} no existe")
            print(f"[!] - El usuario {busqueda} no existe")


def editar_usuario():
    
    print("[!] - EDITAR USUARIO\n")
    #buscar_usuario()
    index_ = buscar_usuario()
    while True:
        
        opcion = input("Editar usuario \n1-nombre\n2-apelldio\n3-direccion\n4-trabajo\n5-Salir\n:> ")
        if opcion == "1":
            
            with open(PATH, 'r') as f:
                f_data = json.load(f)
                
                while True:##EVITAR QUE EL CAMPO QUEDE VACIO
                    cambio = input("nuevo nombre: ")
                    f_data[index_]['nombre'] = cambio
                    if cambio:
                        break
                    else:
                        print("[!] - No puedes dejar el campo vacio")
            with open(PATH, 'w') as f:
                json.dump(f_data , f, indent=2)
                
        elif opcion == "2":
            
            with open(PATH, 'r') as f:
                f_data = json.load(f)
                
                while True:
                    cambio = input("nuevo apellido: ")
                    f_data[index_]['apellido'] = cambio
                    if cambio:
                        break
                    else:
                        print("[!] - No puedes dejar el campo vacio")
            with open(PATH, 'w') as f:
                json.dump(f_data , f, indent=2)
        
        elif opcion == "3":
            
            with open(PATH, 'r') as f:
                f_data = json.load(f)
                
                while True:
                    cambio = input("nueva Direccion : ")
                    f_data[index_]['informacion']['direccion'] = cambio
                    if cambio:
                        break
                    else:
                        print("[!] - No puedes dejar el campo vacio")
            with open(PATH, 'w') as f:
                json.dump(f_data , f, indent=2)
        
        elif opcion == "4":
            
            with open(PATH, 'r') as f:
                f_data = json.load(f)
                
                while True:
                    cambio = input("nuevo Trabajo: ")
                    f_data[index_]['informacion']['trabajo'] = cambio
                    if cambio:
                        break
                    else:
                        print("[!] - No puedes dejar el campo vacio")
            with open(PATH, 'w') as f:
                json.dump(f_data , f, indent=2)
        
        elif opcion == "5":
            print("Usuario actualizado ....")
            buscar_usuario()
            print("Saliendo editor de usuarios...")
            break
        
        else:
            print("Opcion invaida...")


def menu():
    crear_archivos()
    while True:
        
        opcion = input("1.Agregar usuario \n2.Buscar usuario \n3.Editar usuario \n4.Salir \n:> ")

        if opcion == "1":
            agregar_usuario()
            
        elif opcion == "2":
            buscar_usuario()
            
        elif opcion == "3":
            editar_usuario()
        
        elif opcion == "4":
            print("[!] - Saliendo del resgistro de usuarios...")
            break
        else:
            print("Opcion invaida...")

menu()