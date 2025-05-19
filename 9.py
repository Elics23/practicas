datos_personales = {
    "nombre": "Elisabeth Carretero",
    "edad": 18,
    "ciudad": "Madrid",
    "profesion": "Estudiante",
    "correo": "elicarretero121@gmail.com"
}
print("Datos personales:")
for clave, valor in datos_personales.items():
    print(f"{clave.capitalize()}: {valor}")