import itertools
import os

def pedir_datos():
    """Solicita datos del usuario para generar el diccionario."""
    print("Introduce los datos para generar el diccionario:")
    datos = {
        "nombre": input("Nombre: ").strip(),
        "apellido": input("Apellido: ").strip(),
        "nacimiento": input("Fecha de nacimiento (DDMMYYYY): ").strip(),
        "direccion": input("Dirección: ").strip(),
        "ciudad": input("Ciudad: ").strip(),
        "pais": input("País: ").strip(),
        "telefono": input("Teléfono: ").strip(),
        "mascota": input("Nombre de mascota: ").strip(),
        "pareja": input("Nombre de pareja: ").strip(),
        "hijos": input("Nombre de hijos (separados por coma): ").strip().split(","),
        "apodo": input("Apodo: ").strip(),
        "empresa": input("Empresa favorita o donde trabaja: ").strip(),
        "color": input("Color favorito: ").strip(),
        "comida": input("Comida favorita: ").strip(),
        "placa_auto": input("Placa del auto: ").strip(),
        "dni": input("DNI o cédula: ").strip(),
        "hermanos": input("Nombre de hermanos (separados por coma): ").strip().split(","),
        "frases": input("Frases típicas que usa: ").strip().split(","),
        "redes_sociales": input("Redes sociales favoritas (separadas por coma): ").strip().split(","),
        "graduacion": input("Año de graduación: ").strip(),
        "pelicula": input("Película favorita: ").strip(),
        "serie": input("Serie favorita: ").strip(),
        "aniversario": input("Fecha de aniversario (DDMMYYYY): ").strip(),
        "extra": input("Palabras adicionales (separadas por coma): ").strip().split(","),
    }
    return datos

def generar_variaciones(palabra):
    """Genera muchas variaciones de una palabra."""
    if not palabra:
        return []
    
    variaciones = {
        palabra, palabra.lower(), palabra.upper(), palabra.capitalize(),
        palabra[::-1],  # Invertida
        f"{palabra}123", f"{palabra}!", f"{palabra}@", f"{palabra}#",
        f"{palabra}2024", f"{palabra}$", f"{palabra}*", f"{palabra}007",
        f"xX{palabra}Xx", f"Super{palabra}", f"Mega{palabra}", f"{palabra}Pro",
        f"{palabra}_2024", f"{palabra}-2024", f"{palabra}.2024", f"{palabra}2025",
        f"{palabra}!", f"{palabra}@", f"{palabra}#", f"{palabra}*", f"{palabra}$",
        f"{palabra}007", f"{palabra}000", f"{palabra}666", f"{palabra}999",
        palabra.replace("a", "@").replace("o", "0").replace("i", "1").replace("e", "3"),  # Leet básico
    }
    
    return list(variaciones)

def generar_diccionario(datos, nombre_archivo="diccionario"):
    """Genera y guarda el diccionario sin desbordar la memoria."""
    
    palabras_clave = [
        datos["nombre"], datos["apellido"], datos["nacimiento"], datos["direccion"], datos["ciudad"],
        datos["pais"], datos["telefono"], datos["mascota"], datos["pareja"], datos["apodo"],
        datos["empresa"], datos["color"], datos["comida"], datos["placa_auto"], datos["dni"],
        datos["graduacion"], datos["pelicula"], datos["serie"], datos["aniversario"]
    ] + datos["hijos"] + datos["hermanos"] + datos["frases"] + datos["redes_sociales"] + datos["extra"]
    
    palabras_clave = [p.strip() for p in palabras_clave if p.strip()]
    
    total_palabras = 0
    file_count = 1
    max_size = 50_000_000  # Límite de 50 MB por archivo

    with open(f"{nombre_archivo}_{file_count}.txt", "w", encoding="utf-8") as file:
        # Variaciones individuales
        for palabra in palabras_clave:
            variaciones = generar_variaciones(palabra)
            for var in variaciones:
                file.write(var + "\n")
                total_palabras += 1

        # Combinaciones de palabras clave (2, 3, 4 y hasta 5 palabras)
        for r in range(2, 6):  
            for combo in itertools.permutations(palabras_clave, r):
                combinaciones = {
                    "".join(combo), "-".join(combo), "_".join(combo), ".".join(combo),
                    f"{combo[0]}{combo[1]}2024", f"{combo[0]}{combo[1]}007", f"{combo[0]}Mega{combo[1]}",
                    f"{combo[0]}_{combo[1]}_{combo[2]}" if r >= 3 else "",  # Si hay al menos 3 palabras
                    f"{combo[0]}-{combo[1]}-{combo[2]}-{combo[3]}" if r >= 4 else "",  # 4 palabras juntas
                    f"{combo[0]}_{combo[1]}_{combo[2]}_{combo[3]}_{combo[4]}" if r == 5 else "",  # 5 palabras juntas
                }
                for comb in combinaciones:
                    if comb:
                        file.write(comb + "\n")
                        total_palabras += 1

                        # Si el archivo es muy grande, crear uno nuevo
                        if file.tell() > max_size:
                            file.close()
                            file_count += 1
                            file = open(f"{nombre_archivo}_{file_count}.txt", "w", encoding="utf-8")

    print(f"Diccionario guardado en {file_count} archivos con un total de {total_palabras} combinaciones.")

def main():
    print("Generador de diccionarios para ataques de fuerza bruta (hacking ético)")
    datos = pedir_datos()
    generar_diccionario(datos)

if __name__ == "__main__":
    main()
