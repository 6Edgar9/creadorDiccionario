import itertools
import os

def pedir_datos():
    """Solicita datos del usuario para generar el diccionario."""
    print("Introduce los datos para generar el diccionario:")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    nacimiento = input("Fecha de nacimiento (DDMMYYYY): ").strip()
    direccion = input("Dirección: ").strip()
    ciudad = input("Ciudad: ").strip()
    pais = input("País: ").strip()
    telefono = input("Teléfono: ").strip()
    mascota = input("Nombre de mascota: ").strip()
    pareja = input("Nombre de pareja: ").strip()
    hijos = input("Nombre de hijos (separados por coma): ").strip()
    apodo = input("Apodo: ").strip()
    empresa = input("Empresa favorita o donde trabaja: ").strip()
    color = input("Color favorito: ").strip()
    comida = input("Comida favorita: ").strip()
    placa_auto = input("Placa del auto: ").strip()
    dni = input("DNI o cédula: ").strip()
    hermanos = input("Nombre de hermanos (separados por coma): ").strip()
    frases = input("Frases típicas que usa: ").strip()
    redes_sociales = input("Redes sociales favoritas (separadas por coma): ").strip()
    graduacion = input("Año de graduación: ").strip()
    pelicula = input("Película favorita: ").strip()
    serie = input("Serie favorita: ").strip()
    aniversario = input("Fecha de aniversario (DDMMYYYY): ").strip()
    extra = input("Palabras adicionales (separadas por coma): ").strip()

    return {
        "nombre": nombre, "apellido": apellido, "nacimiento": nacimiento,
        "direccion": direccion, "ciudad": ciudad, "pais": pais, "telefono": telefono,
        "mascota": mascota, "pareja": pareja, "hijos": hijos.split(","),
        "apodo": apodo, "empresa": empresa, "color": color, "comida": comida,
        "placa_auto": placa_auto, "dni": dni, "hermanos": hermanos.split(","),
        "frases": frases.split(","), "redes_sociales": redes_sociales.split(","),
        "graduacion": graduacion, "pelicula": pelicula, "serie": serie,
        "aniversario": aniversario, "extra": extra.split(",")
    }

def generar_variaciones(palabras):
    """Genera variaciones con mayúsculas, minúsculas, números y caracteres especiales."""
    variaciones = set()

    for palabra in palabras:
        palabra = palabra.strip()
        if palabra:
            variaciones.add(palabra)
            variaciones.add(palabra.lower())
            variaciones.add(palabra.upper())
            variaciones.add(palabra.capitalize())
            variaciones.add(palabra[::-1])  # Invertida
            variaciones.add(f"{palabra}123")
            variaciones.add(f"{palabra}!")
            variaciones.add(f"{palabra}@")
            variaciones.add(f"{palabra}#")
            variaciones.add(f"{palabra}2024")
            variaciones.add(f"{palabra}$")
            variaciones.add(f"{palabra}*")
            variaciones.add(f"{palabra}007")
    
    return variaciones

def combinar_palabras(datos):
    """Genera combinaciones de palabras clave y variaciones."""
    palabras_clave = [
        datos["nombre"], datos["apellido"], datos["nacimiento"], datos["direccion"], datos["ciudad"],
        datos["pais"], datos["telefono"], datos["mascota"], datos["pareja"], datos["apodo"],
        datos["empresa"], datos["color"], datos["comida"], datos["placa_auto"], datos["dni"],
        datos["graduacion"], datos["pelicula"], datos["serie"], datos["aniversario"]
    ] + datos["hijos"] + datos["hermanos"] + datos["frases"] + datos["redes_sociales"] + datos["extra"]

    # Generar variaciones
    variaciones = generar_variaciones(palabras_clave)

    # Generar combinaciones de palabras
    combinaciones = set()
    for r in range(2, 4):  # Combinaciones de 2 a 3 palabras
        for combo in itertools.permutations(variaciones, r):
            combinaciones.add("".join(combo))
            combinaciones.add("-".join(combo))
            combinaciones.add("_".join(combo))
            combinaciones.add(".".join(combo))

    return variaciones.union(combinaciones)

def guardar_diccionario(diccionario, nombre_archivo="diccionario.txt"):
    """Guarda el diccionario en un archivo de texto."""
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        for palabra in diccionario:
            file.write(palabra + "\n")
    print(f"Diccionario guardado en '{nombre_archivo}' con {len(diccionario)} combinaciones.")

def main():
    print("Generador de diccionarios para ataques de fuerza bruta (hacking ético)")
    datos = pedir_datos()
    diccionario = combinar_palabras(datos)
    guardar_diccionario(diccionario)

if __name__ == "__main__":
    main()
