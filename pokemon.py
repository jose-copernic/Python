import requests

nom = input("Introdueix el nom del Pokémon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + nom.lower()

resposta = requests.get(url)

if resposta.status_code == 200:
    dades = resposta.json()

    print("Nom:", dades["name"].capitalize())
    print("Número Pokédex:", dades["id"])

    tipus = dades["types"][0]["type"]["name"]
    print("Tipus principal:", tipus)

    habilitats = dades["abilities"][0]["ability"]["name"]
    print("habilitats:", habilitats)
    
    habilitats2 = dades["abilities"][1]["ability"]["name"]
    print("habilitats 2:", habilitats2)
    

    imatge = dades["sprites"]["front_default"]
    print("Imatge:", imatge)

else:
    print(" Error: El Pokémon no existeix o el nom està mal escrit.")
