import re


def palabra(data):
    texto = re.sub(r'–', ' ', data)
    list_texto = texto.split()
    len_texto = len(list_texto)
    return len_texto


def copias(sellos):
    cantidad_de_copias = sellos

    return cantidad_de_copias