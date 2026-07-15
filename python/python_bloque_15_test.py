import json

with open("ejemplo3.json", "w", encoding="utf-8") as archivo:

    dicctionary = {
        "alumno": "Edwar",
        "edad": "Viejito",
        "casa": "La de mi mamá"
    }

    #archivo.write(str(dicctionary))
    json.dump(dicctionary, archivo, indent=4, ensure_ascii=False)
