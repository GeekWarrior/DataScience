import pandas as pd
import json
import numpy as np

with open("episodes.json") as arq:
    data = json.load(arq)

#print(data)

episodes = pd.DataFrame(data['episodes'])

#print(episodes.episodeDescription[2])

mortes = pd.read_csv("character-deaths.csv")
#print(mortes.head())

mortes2 = pd.DataFrame(mortes)
#print(mortes2.columns)

#print("Número de mortes: ", mortes.count()["Name"])

aliancas = mortes.groupby("Allegiances")["Name"].count()
#print(aliancas)

genero = mortes.groupby("Gender")["Name"].count()
#print(genero)

livro = mortes.groupby("Book of Death")["Name"].count()
#print(livro)

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (8,8)
#aliancas.plot.bar()
#plt.show()

plt.rcParams['figure.figsize'] = (5,5)
#genero.plot.pie(labels="MH")
#plt.show()

livro.plot.line()
plt.show()

