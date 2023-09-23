import json

Datos={} # creo la variable datos de tipo diccionario
Datos["Clientes"]=[]  # dento de datos que es un diccionario creo una lista
Datos["Clientes"].append({ "Nombre": "Roberto",
                        "Apellido":"Paez",
                        "Edad":53
                        })
Datos["Clientes"].append({ "Nombre": "Alejandro" ,
                            "Apellido": "Rodriguez",
                            "Edad": 50 })

with open("Datos.json", "w") as file:
    json.dump(Datos,file, indent=4)

