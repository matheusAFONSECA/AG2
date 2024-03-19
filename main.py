import pandas as pd
from sklearn.model_selection import train_test_split
import warnings

# Fazer a leitura dos dados utilizando a biblioteca Pandas
dataset = pd.read_csv("palmerpenguins.csv")

# Converter os valores presentes na coluna 'island' para números inteiros, de acordo com o mapeamento
dataset['island'] = dataset['island'].replace({
    "Biscoe": 0,
    "Dream": 1,
    "Torgersen": 2
})
dataset['sex'] = dataset['sex'].replace({
    "FEMALE": 0,
    "MALE": 1
})
dataset['species'] = dataset['sex'].replace({
    "Adeline": 0,
    "Chinstrap": 1,
    "Gentoo": 2
})

# Reordenar as colunas do conjunto de dados
new_col_order = ['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']
dataset = dataset.reindex(columns=new_col_order)

# Separar o conjunto de dados em duas partes:  80% para treinamento e 20% para testes
X = dataset.drop(columns=['species']) # features
y = dataset['species'] # target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
print(f"Tamanho X de treino: {X_train.shape}")
print(f"Tamanho X de teste: {X_test.shape}")
print(f"Tamanho y de treino: {y_train.shape}")
print(f"Tamanho y de teste: {y_test.shape}")

print(dataset.head())
