import hashlib
import json
import os
import itertools

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

def brute_force_attack(dictionary_file):
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
    
    with open(dictionary_file, "r") as file:
        for line in file:
            word = line.strip()
            if hash_password(word) == stored_hash:
                print(f"Contraseña encontrada: {word}")
                return
    
    print("No se encontró la contraseña en el diccionario.")

if __name__ == "__main__":
    while True:
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ataque de fuerza bruta")
        print("4. Salir")
        
        option = input("Seleccione una opción: ")
        if option == "1":
            register()
        elif option == "2":
            login()
        elif option == "3":
            dictionary_file = input("Ingrese el nombre del archivo de diccionario: ")
            brute_force_attack(dictionary_file)
        elif option == "4":
            break
        else:
            print("Opción no válida.")
