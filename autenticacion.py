# autenticacion.py
from usuarios import usuarios

def iniciar_sesion(nombre, contrasena):
    if nombre not in usuarios:
        return "Usuario no encontrado"
    if usuarios[nombre] != contrasena:
        return "Contraseña incorrecta"
    return "Inicio de sesión exitoso"