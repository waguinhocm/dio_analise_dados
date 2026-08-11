import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
"""print(df.head())
print(df.info())"""

"""plt.scatter(df['total_bill'], df['tip'])
plt.xlabel('Conta Total')
plt.ylabel('Valor da Gorjeta')
plt.title('Relação entre Conta e Gorjeta')
plt.show()"""

"""sns.scatterplot(data=df, x='total_bill', y='tip')
plt.show()"""

"""fig = px.scatter(
    df,
    x='total_bill',
    y='tip',
    color='day',
    size='size',
    hover_data=['sex', 'time'],
    title='Relação entre Conta e Gorjeta por Dia da Semana',
)
fig.show()"""

"""plt.figure(figsize=(8, 5))
plt.bar(df['day'], df['tip'], color='skyblue')
plt.xlabel('Dia da Semana')
plt.ylabel('Valor da Gorjeta')
plt.title('Gorjeta por Dia da Semana')
plt.show()"""

"""fig, ax = plt.subplots(1, 2, figsize=(10, 4))

sns.histplot(df['total_bill'], ax=ax[0])
ax[0].set_title('Distribuição da Conta Total')

sns.boxplot(data=df, x='day', y='tip', ax=ax[1])
ax[1].set_title('Gorjeta por Dia da Semana')

plt.show()"""

correlacao = df.corr(numeric_only=True)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlacao,
    annot=True,
    cmap='coolwarm',
)

plt.title('Correlação entre Variáveis Numéricas')

plt.show()
