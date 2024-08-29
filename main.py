import numpy as np
from enum import Enum
from prettytable import PrettyTable
import re

frases = [
    "Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional",
    "Hola, ¿cómo estas?",
    ]

tipos = Enum('Tipos', ['POSITIVO', 'NEUTRAL', 'NEGATIVO'])

palabras_clave = {
    "muerte":tipos.NEGATIVO,
    "pérdida":tipos.NEUTRAL,
    "luto":tipos.NEGATIVO,
    "excelente":tipos.POSITIVO, 
    "gran":tipos.POSITIVO, 
    "positivo":tipos.POSITIVO,
    }


def separar_palabras(frase):
    frase = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚ\s\d]", " ", frase)
    return frase.lower().split()


def calcular_vector_w(frase):
    palabras_en_frase = separar_palabras(frase)
    vector_w = np.zeros((len(palabras_clave)), dtype=int)
    lista_palabras_clave = list(palabras_clave.keys())
    for i in range(len(palabras_clave)):
        if lista_palabras_clave[i] in palabras_en_frase:
            vector_w[i]+=1
    return vector_w


def calcular_vector_s(frase):
    vector_s = np.array([0, 0, 0])
    palabras_en_frase = separar_palabras(frase)
    lista_palabras_clave = list(palabras_clave.keys())
    for palabra in palabras_en_frase:
        if palabra in lista_palabras_clave:
            if palabras_clave.get(palabra) == tipos.POSITIVO:
                vector_s[0]+=1
            elif palabras_clave.get(palabra) == tipos.NEUTRAL:
                vector_s[1]+=1
            elif palabras_clave.get(palabra) == tipos.NEGATIVO:
                vector_s[2]+=1
    return vector_s


def calcular_calidad_promedio(frase):
    vector_w = calcular_vector_w(frase)
    return np.sum(vector_w)/vector_w.size


def calcular_promedio_sentimiento(frase):
    vector_s = calcular_vector_s(frase)
    return np.dot(np.array([1, 0, -1]), vector_s)


print(f"Lista de palabras clave: {list(palabras_clave.keys())}")
t = PrettyTable(['i', 'Frase', 'Vector W', 'Calidad promedio', 'Vector S', 'Promedio de sentimiento'])
for i in range(len(frases)):
    t.add_row([i, frases[i], calcular_vector_w(frases[i]),calcular_calidad_promedio(frases[i]), calcular_vector_s(frases[i]), calcular_promedio_sentimiento(frases[i])])
print(t)

