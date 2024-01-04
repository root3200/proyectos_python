import os
file = "Agenda_telefonica_v3/test.json"
def file_():
    file = "Agenda_telefonica_v3/test.json"
    n1 = os.path.join(os.getcwd(), file)
    #n1 = os.getcwd()
print(os.getcwd())
#     with open(n1, "a") as f:
#         f.write("[\n]")
#     #print(n1)
# try:
#     with open(file, "r") as f:
#         f.read(f)
# except FileNotFoundError as e:
#     if e.strerror == "No such file or directory":
#         file_()