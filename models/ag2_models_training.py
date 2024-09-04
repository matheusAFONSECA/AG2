from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
import json
import pandas as pd

class Training:
    def __init__(self, data) -> None:
        self.data = data  # dataset tratado
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None  # Inicialize o modelo aqui
        # Definindo os mapeamentos para a classificação
        self.island_mapping = {"Biscoe": 0, "Dream": 1, "Torgersen": 2}
        self.sex_mapping = {"F": 0, "M": 1}
        self.specie_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}

    def split_data(self):
        # Realizando a separação dos dados de treinamento e teste
        self.X = self.data.drop(columns=["species"])  # features
        self.y = self.data["species"]  # target
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=0
        )
        print(f"Tamanho X de treino: {self.X_train.shape}")
        print(f"Tamanho X de teste: {self.X_test.shape}")
        print(f"Tamanho y de treino: {self.y_train.shape}")
        print(f"Tamanho y de teste: {self.y_test.shape}")

    def trainning_model(self):
        self.split_data()

        # instanciando o modelo
        self.model = DecisionTreeClassifier()

        # treinando o modelo
        self.model.fit(self.X_train, self.y_train)

        # Realizando a predição
        tree_pred = self.model.predict(self.X_test)

        # Avaliando o modelo
        tree_ava = classification_report(self.y_test, tree_pred)
        print(tree_ava)

        # avaliação por acurácia
        tree_score = accuracy_score(self.y_test, tree_pred)

        print(f"Pontuação de treinamento do modelo: {tree_score}")

        return tree_score
    
    # Função de teste para carregar JSON e realizar a predição
    def test_predict_from_json(self, json_path):
        # Carregar o JSON
        with open(json_path, 'r') as file:
            data = json.load(file)

        # Extrair as informações do JSON
        island = data.get("Ilha")
        sex = data.get("Sexo")
        culmen_length_mm = data.get("Comprimento do culmen (mm)")
        culmen_depth_mm = data.get("Profundidade do culmen (mm)")
        flipper_length_mm = data.get("Comprimento da nadadeira (mm)")
        body_mass_g = data.get("Massa corporal (g)")

        # Mapear os valores categóricos
        island = self.island_mapping.get(island, None)
        sex = self.sex_mapping.get(sex, None)

        # Verificar se os valores mapeados são válidos
        if island is None:
            print("Ilha não reconhecida!")
            return
        if sex is None:
            print("Sexo não reconhecido!")
            return

        # Preparar os dados para o modelo
        dados = pd.DataFrame([{
            'island': island,
            'sex': sex,
            'culmen_length_mm': culmen_length_mm,
            'culmen_depth_mm': culmen_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g
        }])

        # Fazer a predição usando o modelo
        output = self.model.predict(dados)
        output_specie = self.specie_mapping.get(output[0], None)

        # Exibir o resultado da classificação
        print(f"Resultado da classificação: {output_specie}")
