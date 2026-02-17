import random

# lista de palabras
palabras = [
    "elver", "jagua", "cafe", "keyboard", "otorinolaringologia",
    "donaty", "magnanimo", "naruto", "discrepancia", "transeunte",
    "camila", "badbunny", "soto", "braulio", "notengounarealmente"
]

# seleccionar 15 palabras aleatorias sin repetir
palabras_seleccionadas = random.sample(palabras, 15)

errores = 0

for palabra in palabras_seleccionadas:
    print("\nEscribe esta palabra:", palabra)
    entrada_usuario = input("> ")

    if entrada_usuario == palabra:
        print("¡Correcto!")
    else:
        print("Incorrecto")
        errores += 1

print("\nFin del juego")
print("Errores:", errores)



