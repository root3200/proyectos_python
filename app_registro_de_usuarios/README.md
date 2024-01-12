# Aplicacion registro de usuarios.

Aplicacion que registra usuarios a partir de un archivo txt que contiene:

+ Nombre
+ Apellido
+ Oficios
+ Direcciones

> Datos ficticios

Puede buscar y editar usuarios, los datos se almacena en el archivo data.json

**Ejemplo:** 

```json
  {
    "id": "FG1836R",
    "nombre": "Javier",
    "apellido": "Rojas",
    "informacion": {
      "edad": 47,
      "sexo": "H/M/B",
      "direccion": "Avenida de la Esperanza 425",
      "trabajo": "Gerente de Ventas"
    }
```

Despues de crear el usuario se genera un log.json que contiene el id y la fecha.

**Ejemplo**

```json
  {
    "ID": "FG1836R",
    "FECHA": "2024-01-04 01:29"
  }
```
