import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, mean_absolute_error, mean_squared_error, precision_score, r2_score, recall_score
from sklearn.preprocessing import StandardScaler

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

df = pd.read_csv(url)
print(df.head())
"""print(df.info())"""

df = df.dropna()  # apagar linhas com valores nulos
x = df.drop("median_house_value", axis=1)  # x recebe todas as colunas menos a coluna median_house_value
x = pd.get_dummies(x)  # transformar variáveis categóricas (no caso a coluna ocean_proximity) em variáveis dummy
y = df["median_house_value"]  # y recebe a coluna median_house_value que foi retirada de x

x_train, x_test, y_train, y_test = train_test_split(  # dividir os dados em conjuntos de treinamento e teste
    x, y, test_size=0.2, random_state=42  # test_size=0.2 20% dos dados serão usados para teste e 80% para treinamento, random_state=42 garante que a divisão seja reproduzível
)

model = LinearRegression()  # criar o modelo de regressão linear
model.fit(x_train, y_train)  # treinar o modelo com os dados de treinamento

y_pred = model.predict(x_test)  # fazer previsões com os dados de teste

residuos = y_test - y_pred  # calcular os resíduos (diferença entre os valores reais e os valores previstos)

"""plt.figure(figsize=(6, 5))

plt.scatter(y_pred, residuos)

plt.axhline(0, color='red')  # linha horizontal no 0 para referência

plt.xlabel('Valores Previstos')
plt.ylabel('Resíduos')
plt.title('Resíduos vs Valores Previstos')
plt.show()

plt.figure(figsize=(6, 5))
sns.histplot(residuos, kde=True)  # histograma dos resíduos com curva de densidade
plt.title('Distribuição dos Resíduos')
plt.show()"""

"""mae = mean_absolute_error(y_test, y_pred)  # calcular o erro absoluto médio
print(f'Mean Absolute Error: {mae}')  # imprimir o erro absoluto médio

mse = mean_squared_error(y_test, y_pred)  # calcular o erro quadrático médio
print(f'Mean Squared Error: {mse}')  # imprimir o erro quadrático médio

rmse = np.sqrt(mse)  # calcular a raiz quadrada do erro quadrático médio
print(f'Root Mean Squared Error: {rmse}')  # imprimir a raiz quadrada do erro quadrático médio

mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100  # calcular o erro percentual médio absoluto
print(f'Mean Absolute Percentage Error: {mape}%')  # imprimir o erro percentual médio absoluto

r2 = r2_score(y_test, y_pred)  # calcular o coeficiente de determinação R²
print(f'R² Score: {r2}')  # imprimir o coeficiente de determinação R²

metrics = pd.DataFrame({
    "MAE": [mae],
    "MSE": [mse],
    "RMSE": [rmse],
    "MAPE": [mape],
    "R²": [r2]
})
print(metrics)

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # linha de referência y=x
plt.xlabel('Valores Reais')
plt.ylabel('Valores Previstos')
plt.title('Valores Reais vs Valores Previstos')
plt.show()"""

"""plt.figure(figsize=(8, 5))
plt.scatter(df['median_income'], df['total_rooms'], alpha=0.5)

plt.xlabel('Renda Média')
plt.ylabel('Número Total de Quartos')
plt.title('Relação entre Renda Média e Número Total de Quartos')
plt.show()"""

"""df_class = df.copy()  # criar uma cópia do dataframe original para classificação
df_class['higPrice'] = (
    df_class['median_house_value'] >
    df_class['median_house_value'].median()
    ).astype(int)  # criar uma nova coluna 'highPrice' que indica se o valor da casa é maior que a mediana
print(df_class.head())

x = df_class.drop(["median_house_value", "higPrice"], axis=1)  # x recebe todas as colunas menos as colunas median_house_value e highPrice
x = pd.get_dummies(x)  # transformar variáveis categóricas em variáveis dummy
y = df_class["higPrice"]  # y recebe a coluna highPrice
x_train, x_test, y_train, y_test = train_test_split(  # dividir os dados em conjuntos de treinamento e teste
    x, y, test_size=0.2, random_state=42  # test_size=0.2 20% dos dados serão usados para teste e 80% para treinamento, random_state=42 garante que a divisão seja reproduzível
)

clf = LogisticRegression(max_iter=1000)  # criar o modelo de regressão logística
clf.fit(x_train, y_train)  # treinar o modelo
y_pred = clf.predict(x_test)  # fazer previsões com os dados de teste

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)
plt.xlabel('Classe Prevista')
plt.ylabel('Classe Real')
plt.title('Matriz de Confusão')
plt.show()

accuracy = accuracy_score(y_test, y_pred)  # calcular a acurácia do modelo
print(f'Accuracy: {accuracy}')

precision = precision_score(y_test, y_pred)  # calcular a precisão do modelo
print(f'Precision: {precision}')

recall = recall_score(y_test, y_pred)  # calcular o recall do modelo
print(f'Recall: {recall}')

f1 = f1_score(y_test, y_pred)  # calcular o F1-score do modelo
print(f'F1 Score: {f1}')

print(f'Classification Report:\n{classification_report(y_test, y_pred)}')"""
"""accuracy - qual a taxa geral de acertos do modelo, ou seja, a proporção de previsões corretas em relação ao total de previsões feitas.
precision - qual a proporção de verdadeiros positivos em relação ao total de positivos previstos pelo modelo.
    Em outras palavras, mede a capacidade do modelo de não classificar como positivo um exemplo que é realmente negativo.
recall - qual a proporção de verdadeiros positivos em relação ao total de positivos reais.
    Em outras palavras, mede a capacidade do modelo de encontrar todos os exemplos positivos.
f1 - é a média harmônica entre precisão e recall, fornecendo uma medida balanceada do desempenho do modelo."""

"""wss = []
k_range = range(1, 10)
X_cluster = df[['median_house_value', 'median_income']]  # selecionar as colunas median_income e median_house_value para o clustering

for k in k_range:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_cluster)

    wss.append(model.inertia_)

plt.plot(k_range, wss, marker='o')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('WSS')
plt.title('Método do Cotovelo para Determinar o Número Ideal de Clusters')
plt.show()"""
