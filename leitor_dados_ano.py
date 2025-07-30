import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dados_filmes200.csv")
an = dados["ano"].value_counts().sort_index()
plt.bar(an.index, an.values)
plt.title("Quantidades de filmes produzidos por ano entre os 200 melhores filmes")
plt.xlabel("Anos")
plt.ylabel("Quantidades")
plt.tight_layout()
plt.show()
