# usuarios.py
usuarios = {}

def registrar_usuario(nombre, contrasena):
    if nombre in usuarios:
        return "Error: Usuario ya registrado"
    usuarios[nombre] = contrasena
    return "Usuario registrado"
