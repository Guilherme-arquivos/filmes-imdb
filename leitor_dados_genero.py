import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dados_filmes200.csv")
gen = dados["genero"].value_counts()

plt.pie(gen, labels=gen.index, autopct='%1.2f%%')
plt.axis("equal")
plt.title("Gráfico que mostra a participação de cada gênero entre os 200 filmes mais bem avaliados")
plt.show()