# creadorDiccionario

**creadorDiccionario** es un proyecto educativo que contiene dos herramientas principales:

1. `dic.py` — Generador de diccionarios a partir de información del usuario.  
   - Crea variaciones y combinaciones de palabras clave para formar listas (diccionarios) de contraseñas posibles.
   - Divide la salida en varios archivos si supera un tamaño configurado.
2. `ataque.py` — Script simple para registrar usuarios (con contraseña hasheada) y probar ataques de fuerza bruta usando los diccionarios generados.

---

## ⚠️ Advertencia legal y ética

Estas herramientas son *doble uso* (dual-use). Pueden emplearse para pruebas de seguridad y educación (hacking ético), **pero también pueden utilizarse para actividades ilícitas**.  
**Úsalas únicamente en entornos controlados y con cuentas/servicios que poseas o para los que tengas permiso explícito**. El autor no se responsabiliza del uso indebido.

---

## 📦 Contenido del repositorio

- `dic.py` — Generador de diccionarios (entrada interactiva).
- `ataque.py` — Registro/login de usuarios y función de fuerza bruta que prueba diccionarios.
- `.gitignore` — Ignora archivos temporales, datos sensibles y salidas grandes.

---

## 🔧 Requisitos

- Python 3.8+ (se usan solo librerías estándar)
- Espacio en disco suficiente para generar los archivos de diccionario (pueden ser grandes).
- Preferible tener una memoria mínima de RAM 32GB para no tener ningún inconveniente

---

## ⚙️ Instalación y uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/creadorDiccionario.git
   cd creadorDiccionario
   ```

2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows
   ```

3. Ejecutar el generador de diccionarios:
   ```bash
   python dic.py
   ```
   - Sigue las preguntas interactivas para introducir datos (nombre, apellidos, fechas, apodos, etc.).
   - El script generará archivos `diccionario_1.txt`, `diccionario_2.txt`, ... en el directorio actual.

4. Registrar un usuario de prueba:
   ```bash
   python ataque.py
   ```
   - Selecciona la opción **1** para registrar un usuario (se guarda en `users.json`).
   - *Nota:* `ataque.py` usa SHA-256 para almacenar el hash de la contraseña.

5. Probar fuerza bruta:
   - En `ataque.py` elige la opción **3** para atacar un usuario y el script buscará en los archivos `diccionario_*.txt`.

---

## 🛡️ Recomendaciones de seguridad (para uso responsable y mejoras)

Si tu objetivo es **probar seguridad** o aprender buenas prácticas, considera mejorar el proyecto así:

- **No almacenar contraseñas en texto plano ni con hash simple**:
  - Sustituir SHA-256 por `bcrypt` o `argon2` con sal única por usuario.
- **Limitar la generación masiva en disco**:
  - Comprimir los diccionarios o generar on-the-fly durante las pruebas.
- **Controlar el tamaño y el rendimiento**:
  - Añadir opciones para filtrar o limitar combinaciones (por longitud, símbolos, etc.).
- **Registro y auditoría**:
  - Mantener logs con permisos restringidos y rotación de archivos.
- **Entornos de prueba**:
  - Usa máquinas virtuales o contenedores aislados para pruebas y evita redes públicas.
- **Protecciones en el lado del servidor** (si pruebas un servicio real):
  - Rate limiting, bloqueo de IP, autenticación multifactor, monitoreo de intentos de login.

---

## 🧪 Buenas prácticas para pruebas (ética)

- Solo prueba cuentas que poseas o donde tengas autorización explícita por escrito.
- Mantén un alcance claro y un plan de pruebas.
- Notifica y coordina con el propietario del sistema antes de realizar pruebas invasivas.
- Borra los datos y resultados cuando termines las pruebas.

---

## 📝 Posibles mejoras (lista corta)

- Añadir argumentos de línea de comandos para controlar la generación (`--max-size`, `--combine-level`, `--output`).
- Añadir filtros (longitud mínima/máxima, inclusión/exclusión de símbolos).
- Implementar generación "streaming" para evitar escritura masiva a disco.
- Añadir pruebas unitarias y validación de entradas.
- Añadir cifrado para archivos sensibles de salida (si se requieren guardar).

---

## 📄 Licencia

Proyecto con licencia **MIT** — ver `LICENSE` si lo añades al repositorio.

---

#### Dios, Assembly y la Patria
#### Edrem

Proyecto educativo — úsalo para aprender sobre generación de diccionarios y seguridad defensiva.
