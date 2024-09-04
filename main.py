from utils.ag2_utils import Utils
from models.ag2_models_training import Training

utils = Utils("data\palmerpenguins.csv")
utils.red_dataset()
data = utils.data_treatment()

training = Training(data)

training_model_score = training.trainning_model()

utils.plot_graphic(training_model_score)

json_data = "Json/test.json"
training.test_predict_from_json(json_data)