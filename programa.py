import json
from usuario import Usuario

usuarios = []
errores = []

def registrar_error(mensaje):
    with open('error.log', 'a') as log:
        log.write(mensaje + '\n')

with open('usuarios.txt', 'r') as file:
    for linea in file:
        try:
            datos_usuario = json.loads(linea)
            usuario = Usuario(**datos_usuario)
            usuarios.append(usuario)
        except json.JSONDecodeError as e:
            registrar_error(f"Error de JSON en la línea: {linea.strip()} - Error: {e}")
        except TypeError as e:
            registrar_error(f"Error en los datos del usuario: {linea.strip()} - Error: {e}")
        except Exception as e:
            registrar_error(f"Error desconocido: {linea.strip()} - Error: {e}")

for usuario in usuarios:
    print(usuario)
