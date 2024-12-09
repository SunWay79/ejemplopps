# usuarios.py
usuarios = {}

def registrar_usuario(nombre, contrasena):
    if nombre in usuarios:
        return "Usuario ya registrado"
    usuarios[nombre] = contrasena
    return "Usuario registrado"