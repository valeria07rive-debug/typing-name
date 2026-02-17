import random


palabras = [
    "elver", "jagua", "cafe", "estupefacto", "otorinolaringologia",
    "donaty", "magnanimo", "naruto", "discrepancia", "transeunte",
    "camila", "badbunny", "soto", "braulio", "notengounarealmente"
]


palabras_seleccionadas = random.sample(palabras, 15)

errores = 0
correctas = 0


for palabra in palabras_seleccionadas:
    print("\nEscribe esta palabra:", palabra)
    entrada_usuario = input("> ")

    if entrada_usuario == palabra:
    print("¡Correcto!")
    correctas += 1
else:
    print("Incorrecto")
    errores += 1


print("\nFin del juego")
print("Errores:", errores)

total = len(palabras_seleccionadas)
accuracy = (correctas / total) * 100

print("Palabras correctas:", correctas)
print("Errores:", errores)
print(f"Exactitud final: {accuracy:.2f}%")




