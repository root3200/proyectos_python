import json
import random


#AGENDA TELEFONICA 
##UBICACIO DEL ARCHIVO JSON
path ="/home/r4m3200/Escritorio/python_ejercicios/Agenda_telefonica_v3/data.json"
path2 ="/home/r4m3200/Escritorio/python_ejercicios/Agenda_telefonica_v3/nombre_apellidos_direcciones_oficios.txt"

opcion = input("1.Agregar usuario \n2.Buscar usuario \n:> ")
while True:
    opcion = input("1.Agregar usuario \n2.Buscar usuario \n3.Editar usuario \n4.Salir \n:> ")
    ##AGREGAR USUARIO
    if opcion == "1":
        
        ##NOMBRE,APELLIDO,DRIECCIONES,OFICIOS ALEATORIO
        with open(path2, "r", encoding='utf-8',) as f:
            f_dara = f.readlines()
            n2= random.choice(f_dara)
            n3 = n2.strip().split(',')
            
        ##ESTRUCTURA JSON
        data = {
            "id": f"FG{random.randint(1000,9999)}R",
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
        print("Agregar usuario")
        ##ABRIR ARCHIVO JSON MODO LECTURA
        with open(path, "r") as f:
            f_data = json.load(f)
            f_data.append(data)
        ##ABRIR ARCHIVO JSON MODO ESCRITURA
        with open(path, "w") as f:
            json.dump(f_data, f, indent=2)

    ##BUSCAR USUARIO
    elif opcion == "2":
        print("Buscar usuario")
        ##ABRIR ARCHIVO JSON MODO LECTURA
        with open(path, "r") as f:
            f_data = json.load(f)
            busqueda = "Marcooooo"
            existe = False
            for i in f_data:
                if busqueda == i['nombre']:
                    print(f"Usuaruaio {i['id']} econtrado \n\tNombre: {i['nombre']} \n\tApellido: {i['apellido']} \n\tInformacion: \n\t\tEdad: {i['informacion']['edad']} \n\t\tSexo: {i['informacion']['sexo']} \n\t\tDireccion: {i['informacion']['direccion']} \n\t\tTrabajo: {i['informacion']['trabajo']}")
                    existe = True
                    break
                            
            if not existe:
                #print(f"[!] - El usuario {busqueda} no existe")
                print(f"[!] - El usuario {busqueda} no existe")
    
    elif opcion == "3":
        print("modificar usuario")
        
#         with open(path, "r") as f:
#             f_data = json.load(f)
#     ##SALIR DE APP            
#     elif opcion == "4":
#         print("Saliendo ...")
#         break
#     ##ERROR DE OPCIONE
#     else:
#         print("Opcion invaida...")

# print("Editar usuario \n1-nombre\n2-apelldio")
# opcion = "2"

# if opcion == "1":
    
#     with open(path, "r") as f:
#         f_data = json.load(f)
#         print(len(f_data[0]['informacion']))
        
#         while True:##BUCLE PARA EVITAR  QUE EL CAMPO QUEDE VACIO 
#             cambio = input("Nuevo nombre: ")
#             f_data[0]['nombre'] = cambio
#             if cambio:
#                 break
#             else:
#                 print("[!] - No puedes dejar el campo vacio")
#     with open(path, "w") as f:
#         json.dump(f_data, f, indent=2)

# if opcion == "2":
    
#     with open(path, "r") as f:
#         f_data = json.load(f)
#         actual = f_data[0]['apellido']
        
#         while True:
#             cambio = input("Nuevo apellido: ")
#             f_data[0]['apellido'] = cambio
#             if cambio:
#                 break
#             else:
#                 print("[!] - No puedes dejar el campo vacio")
        
#     with open(path, "w") as f:
#         json.dump(f_data, f, indent=2)


# with open(path2, "r", encoding='utf-8',) as f:
#     f_dara = f.readlines()
    
#     #diccionario = {}
#     n2 = random.choice(f_dara)
#     n3 = n2.strip().split(',')
#     print(n3[0])

