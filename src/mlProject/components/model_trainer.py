import pandas as pd
import os
from mlProject import logger
from statsmodels.tsa.arima.model import ARIMA
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        model = ARIMA(train_y, order=self.config.order)
        model_fit = model.fit()

         # Ensure the directory exists
        model_dir = os.path.join(self.config.root_dir, 'model_trainer')
        os.makedirs(model_dir, exist_ok=True)

        joblib.dump(model_fit, os.path.join(self.config.root_dir, self.config.model_name))
