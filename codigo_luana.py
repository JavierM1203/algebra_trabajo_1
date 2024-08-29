#frases y palabras dadas en el informe:
palabras = {
    "muerte": "negativa",
    "pérdida": "neutral",
    "luto": "negativa",
    "excelente": "positiva",
    "gran": "positiva",
    "positivo": "positiva",
    "incertidumbre": "negativa",
    "felicidad": "positiva",
    "tranquilidad": "neutral",
    "alegría":"positiva",
    "victorias":"positiva",
    "impactando":"neutral",
    "crecimiento":"neutral",
    "llora":"negativa",
    "perdidas":"negativa",
    "trágico":"negativa",
    "devastación": "negativa"
}
frasesParaAnalizar = [
    "Excelente en su área, su muerte es una enormel",
    "Vaya señora que bueno que se asesora por algui",
    "Se me ocurre y sin ir a clase me informéis por",
    "Soy docente universitario, estoy intentando pr",
     "La pérdida deja una marca que no se borra fácilmente.",
    "La tristeza se cuela en los rincones más profundos del alma.",
    "Hoy todo fluye con una tranquila normalidad.",
    "La felicidad se refleja en los pequeños detalles del día a día.",
    "Hay una alegría tranquila que me acompaña hoy.",
    "Las pequeñas victorias hacen que todo valga la pena.",
    "Es un día como cualquier otro, sin más.",
    "La inflación continúa impactando el poder adquisitivo de los ciudadanos.",
    "El mercado de valores cerró a la baja tras una jornada de incertidumbre.",
    "Las nuevas políticas fiscales buscan estimular el crecimiento económico.",
    "El desempleo ha alcanzado su nivel más bajo en la última década.",
    "El precio del petróleo se mantiene volátil debido a la tensión internacional.",
    "La comunidad llora la pérdida de un líder querido.",
    "El accidente dejó un saldo trágico, con varias vidas perdidas.",
    "Las imágenes de la devastación han conmovido al mundo entero."

]


def vectores(frase, palabras):
    w = []
    s = [0, 0, 0]  # [positiva, neutral, negativa]

    for palabra in palabras.keys():
        if palabra in frase:
            w.append(1)
            #aumento el contador segun la frase si espositiva, neutral o negativa
            if palabras[palabra] == "positiva":
                s[0] += 1
            elif palabras[palabra] == "neutral":
                s[1] += 1
            elif palabras[palabra] == "negativa":
                s[2] += 1
        else:
            w.append(0)
    return w, s
    #devuelvo los vectores w y s

# calidad promedio y promedio de sentimiento
resultados = []
for frase in frasesParaAnalizar:
    w, s = vectores(frase, palabras)
    #calculo del promedio
    prommm = sum(w) / len(w)
    sentimiento = (1 * s[0]) + (0 * s[1]) + (-1 * s[2])
    resultados.append((frase, prommm, sentimiento))

#print analisis de las frases
import pandas as pd
print(".............................")
prueba = pd.DataFrame(resultados, columns=["Frase", "Calidadpromedio", "Sentimientopromedio"])
print(".............................")
print(prueba)
print(".............................")

frase_positiva =prueba.loc[prueba['Sentimientopromedio'].idxmax()]['Frase']
frase_negativa =prueba.loc[prueba['Sentimientopromedio'].idxmin()]['Frase']
print(".............................")

print("-La frase más positiva:", frase_positiva)

print("-la frase más negativa:", frase_negativa)

print(".............................")