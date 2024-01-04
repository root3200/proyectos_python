from datetime import datetime
import json
n1 = datetime.now()
PATH3 = "/home/r4m3200/Escritorio/python_ejercicios/Agenda_telefonica_v3/log.json"

print(n1.strftime("%Y-%m-%d %H:%M"))
def data_():
    id_ = "test_ID"
    n1 = datetime.now()
    fecha_ = n1.strftime("%Y-%m-%d %H:%M")
    data_log = {
        "id": f"FG{id_}R",
        "fecha": f"{fecha_}"
        }
    with open(PATH3, "r") as f:
        f_data = json.load(f)
        f_data.append(data_log)
    with open(PATH3, "w") as f:
        json.dump(f_data, f, indent=2)

data_()