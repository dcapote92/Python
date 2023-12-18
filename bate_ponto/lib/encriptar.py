""" Daniel V.
    Junho de 2023
"""
from cryptography.fernet import Fernet


f = Fernet(b'xZCMaJGHgwUDpMVreS6TUdfgp6PA1JVGn-n8Apm21pU=')

def encriptar(valor):
    """_summary_
    Args:
        valor (string): valor real
    Returns:
        bytes: valor encriptado
    """
    senha = f.encrypt(bytes(valor))
    return senha

def desencriptar(valor):
    """_summary_
    Args:
        valor (bytes): valor encriptado
    Returns:
        bytes: valor real
    """
    return f.decrypt(valor)
