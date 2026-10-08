import numpy as np
import pandas as pd
import tensorflow as tf
from dataloader.dataloader import DataLoader
from utils.logger import get_logger
from .base_model import BaseModel
from executor.trainer import Trainer
LOG = get_logger('click')


class CLICK(BaseModel):
    """FAKE CLICK Model Class"""

    def __init__(self, config):
        super().__init__(config)
        self.model = None
        self.dataset = None
        self.test_dataset = None
        self.info = None
        self.batch_size = self.config.train.batch_size
        self.epoches = self.config.train.epoches
        self.metrics = self.config.train.metrics
        self.validation_steps = 0
        self.train_length = 0
        self.steps_per_epoch = 0
        self.input = 31
        self.out = 2
        self.X_train = []
        self.X_test = []
        self.Y_train = []
        self.Y_test = []

    def load_data(self):
        """Loads and Preprocess data """
        LOG.info(f'Loading {self.config.data.path} dataset...')
        self.dataset = DataLoader().load_data(self.config.data)
        self.dataset = self.dataset.drop('Unnamed: 0',axis=1)
        self.X_train, self.X_test, self.Y_train, self.Y_test = DataLoader.preprocess_data(self.dataset)

    def build(self):
        """ Builds the Tensorflow model based """
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(self.input, activation='relu', input_shape=(self.X_train.shape[1],)),
            tf.keras.layers.Dense(64, activation='sigmoid'),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.4),
            tf.keras.layers.Dense(32, activation='sigmoid'),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.4),
            tf.keras.layers.Dense(25, activation='sigmoid'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])


        LOG.info('Tensorflow Model was built successfully')

    def train(self):
        """Compiles and trains the model"""
        LOG.info('Training started...')

        trainer = Trainer(self.model, self.X_train, self.Y_train, self.X_test, self.Y_test, self.batch_size, self.metrics, self.epoches)
        trainer.train()


    def load_test_data(self):
        """Loads and Preprocess data """
        LOG.info(f'Loading {self.config.test_data.path} dataset...')
        self.test_dataset = DataLoader().load_test_data(self.config.test_data)
        self.test_dataset = DataLoader.preprocess_test_data(self.test_dataset)
        # print(self.test_dataset)


    def evaluate(self):
        """Predicts resuts for the test dataset"""
        predictions = []
        LOG.info(f'Predicting for test dataset')
        LOG.info(f'Predicting')
        predictor_cols = ['UserId', 'Event_click_ad', 'Event_click_carrousel','Event_phone_call', 'Event_send_email', 'Event_send_sms','Category_Holidays', 'Category_Jobs', 'Category_Leisure','Category_Motor', 'Category_Phone', 'Category_Real_State']
        test_X = self.test_dataset[predictor_cols].astype(np.float32).copy()
        # Use the model to make predictions
        predicted_results = self.model.predict(test_X)
        # print(predicted_results)
        test_X['Predictions'] = predicted_results
        test_X['Fake_Prediction'] = np.where(test_X['Predictions'] < 0.5, 0, 1)
        print(test_X.head())
        test_X.to_csv("Final_Fake_prediction",columns= ['UserId', 'Event_click_ad', 'Event_click_carrousel','Event_phone_call', 'Event_send_email', 'Event_send_sms','Category_Holidays', 'Category_Jobs', 'Category_Leisure','Category_Motor', 'Category_Phone', 'Category_Real_State','Fake_Prediction'],index=False)
