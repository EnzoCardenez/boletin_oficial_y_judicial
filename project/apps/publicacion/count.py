import re


def palabra(data):
    texto = re.sub(r'–', ' ', data)
    list_texto = texto.split()
    len_texto = len(list_texto)
    return len_texto


def copias(dias_de_publicacion, copias_requeridas):

    return dias_de_publicacion if copias_requeridas else 0
