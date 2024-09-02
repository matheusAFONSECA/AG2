# trabalhar com dados
import pandas as pd

# separação dos dados do dados para treinamento
from sklearn.model_selection import train_test_split

# avaliação de metricas
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Importação da biblioteca para a criação do modelo de classificação
from sklearn.tree import DecisionTreeClassifier

# plotar gráficos
import matplotlib.pyplot as plt

# leitura do dataset
dataset = pd.read_csv("palmerpenguins.csv")

# Exibindo as primeiras linhas do dataset
dataset.head()

# Tratamento de dados do dataset
dataset['island'] = dataset['island'].replace({
    "Biscoe": 0,
    "Dream": 1,
    "Torgersen": 2
})

dataset['sex'] = dataset['sex'].replace({
    "FEMALE": 0,
    "MALE": 1
})

dataset['species'] = dataset['species'].replace({
    "Adelie": 0,
    "Chinstrap": 1,
    "Gentoo": 2
})

# Reorganizando as colunas do dataset
new_col_order = ['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']
dataset = dataset.reindex(columns=new_col_order)

# Exibindo as primeiras linhas do dataset - apoós tratamento
dataset.head()

# Realizando a separação dos dados de treinamento e teste
X = dataset.drop(columns=['species']) # features
y = dataset['species'] # target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
print(f"Tamanho X de treino: {X_train.shape}")
print(f"Tamanho X de teste: {X_test.shape}")
print(f"Tamanho y de treino: {y_train.shape}")
print(f"Tamanho y de teste: {y_test.shape}")

# instanciando o modelo
tree = DecisionTreeClassifier()

# treinando o modelo
tree.fit(X_train, y_train)

# Realizando a predição
tree_pred = tree.predict(X_test)

# Avaliando o modelo
tree_ava = classification_report(y_test, tree_pred)
print(tree_ava)

# prevendo valores
tree_predict = tree.predict(X_test)         

# avaliação por acurácia
tree_score = accuracy_score(y_test, tree_predict)

print(f"Pontuação de treinamento do modelo: {tree_score}")

# gráfico da acurácia
plt.figure(figsize = (8,4))
plt.title("Model accuracy")
plt.bar(x = [0], height = [tree_score], color = "blue")
plt.xticks([0], ["Tree"])
plt.ylim(0.8,1.05)
plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.grid()
plt.savefig("accuracy.png")
plt.show()

# testando o modelo
# Solicitação de entrada dos parâmetros
island = input("Digite o nome da ilha: ")
sex = input("Digite o sexo (M ou F): ")
culmen_length_mm = float(input("Digite o comprimento do culmen em milímetros: "))
culmen_depth_mm = float(input("Digite a profundidade do culmen em milímetros: "))
flipper_length_mm = float(input("Digite o comprimento da nadadeira em milímetros: "))
body_mass_g = float(input("Digite a massa corporal em gramas: "))

# Exibição dos parâmetros digitados
print("\nParâmetros:")
print("Ilha:", island)
print("Sexo:", sex)
print("Comprimento do culmen (mm):", culmen_length_mm)
print("Profundidade do culmen (mm):", culmen_depth_mm)
print("Comprimento da nadadeira (mm):", flipper_length_mm)
print("Massa corporal (g):", body_mass_g)

