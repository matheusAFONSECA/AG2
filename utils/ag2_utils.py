import pandas as pd

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
        })

        self.data['sex'] = self.data['sex'].replace({
            "FEMALE": 0,
            "MALE": 1
        })

        self.data['species'] =self.data['species'].replace({
            "Adelie": 0,
            "Chinstrap": 1,
            "Gentoo": 2
        })

        # Reorganizando as colunas do dataset
        new_col_order = ['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']
        self.data = self.data.reindex(columns=new_col_order)

        # print(self.data.head(5))