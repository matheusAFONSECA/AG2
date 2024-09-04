import pandas as pd
import matplotlib.pyplot as plt

# Definir opção global para o comportamento futuro sem warnings
pd.set_option('future.no_silent_downcasting', True)

class Utils:
    def __init__(self, dataset):
        self.dataset = dataset      # relative path to the dataset
        self.data = None

    def red_dataset(self):
        # leitura do dataset
        self.data = pd.read_csv(self.dataset)

    def data_treatment(self):
        # Tratamento de dados do dataset
        self.data['island'] = self.data['island'].replace({
            "Biscoe": 0,
            "Dream": 1,
            "Torgersen": 2
        }).infer_objects(copy=False)

        self.data['sex'] = self.data['sex'].replace({
            "FEMALE": 0,
            "MALE": 1
        }).infer_objects(copy=False)

        self.data['species'] = self.data['species'].replace({
            "Adelie": 0,
            "Chinstrap": 1,
            "Gentoo": 2
        }).infer_objects(copy=False)

        # Reorganizando as colunas do dataset
        new_col_order = ['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']
        self.data = self.data.reindex(columns=new_col_order)

        print("Dataset Formatado")
        print(self.data.head(5))

        return self.data
    
    def plot_graphic(self, model_score):
        # gráfico da acurácia
        plt.figure(figsize = (8,4))
        plt.title("Model accuracy")
        plt.bar(x = [0], height = [model_score], color = "blue")
        plt.xticks([0], ["Tree"])
        plt.ylim(0.8,1.05)
        plt.ylabel("Accuracy")
        plt.xlabel("Model")
        plt.grid()
        plt.savefig("grafics/accuracy.png")
        plt.show()
