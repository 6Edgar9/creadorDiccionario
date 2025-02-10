import hashlib
import json
import os
import glob

db_file = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    hashed_password = hash_password(password)
    
    if os.path.exists(db_file):
        with open(db_file, "r") as file:
            users = json.load(file)
    else:
        users = {}
    
    if username in users:
        print("El usuario ya existe.")
        return
    
    users[username] = hashed_password
    with open(db_file, "w") as file:
        json.dump(users, file, indent=4)
    print("Usuario registrado con éxito.")

def login():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if not os.path.exists(db_file):
        print("No hay usuarios registrados.")
        return
    
    with open(db_file, "r") as file:
        users = json.load(file)
    
    if username in users and users[username] == hash_password(password):
        print("Inicio de sesión exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

def brute_force_attack():
    username = input("Ingrese el nombre de usuario a atacar: ")
    
    if not os.path.exists(db_file):
        print("No hay usuarios registrados.")
        return
    
    with open(db_file, "r") as file:
        users = json.load(file)
    
    if username not in users:
        print("Usuario no encontrado.")
        return
    
    stored_hash = users[username]
    
    # Buscar todos los archivos de diccionario
    dictionary_files = glob.glob("diccionario_*.txt")
    
    if not dictionary_files:
        print("No se encontraron archivos de diccionario.")
        return
    
    print(f"Archivos de diccionario encontrados: {len(dictionary_files)}")

    # Probar contraseñas en todos los archivos encontrados
    for dictionary_file in dictionary_files:
        print(f"Probando con {dictionary_file}...")
        with open(dictionary_file, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                if hash_password(word) == stored_hash:
                    print(f"✅ Contraseña encontrada: {word}")
                    return
    
    print("❌ No se encontró la contraseña en los diccionarios.")

if __name__ == "__main__":
    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ataque de fuerza bruta")
        print("4. Salir")
        
        option = input("Seleccione una opción: ")
        if option == "1":
            register()
        elif option == "2":
            login()
        elif option == "3":
            brute_force_attack()
        elif option == "4":
            break
        else:
            print("Opción no válida.")
