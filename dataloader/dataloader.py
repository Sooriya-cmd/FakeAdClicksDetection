"""Data Loader"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


class DataLoader:
    """Data Loader class"""

    @staticmethod
    def load_data(data_config):
        """Loads dataset from path"""
        return pd.read_csv(data_config.path)

    @staticmethod
    def load_test_data(data_config):
        """Loads test dataset from path"""
        return pd.read_csv(data_config.path)

    @staticmethod
    def preprocess_data(dataset):
        """ Preprocess and splits into training and test"""

        labelencoder_X = LabelEncoder()
        dataset.UserId = labelencoder_X.fit_transform(dataset.UserId)
        dataset = pd.get_dummies(dataset, columns = ['Event', 'Category'])
        scaler= MinMaxScaler()
        dataset['UserId'] = scaler.fit_transform(dataset[['UserId']])
        features = dataset.drop(columns=['Fake']).to_numpy(dtype=np.float32)
        target = dataset['Fake'].to_numpy(dtype=np.int32)
        smote = SMOTE(random_state=888)
        X_resampled, y_resampled = smote.fit_resample(features, target)
        X_train, X_test, Y_train, Y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
        return X_train, X_test, Y_train, Y_test

    @staticmethod
    def preprocess_test_data(test_dataset):
        """ Preprocess test"""
        # print(test_dataset)
        labelencoder_X = LabelEncoder()
        test_dataset.UserId = labelencoder_X.fit_transform(test_dataset.UserId)
        test_dataset = pd.get_dummies(test_dataset, columns = ['Event', 'Category'])
        scaler= MinMaxScaler()
        test_dataset['UserId'] = scaler.fit_transform(test_dataset[['UserId']])
        return test_dataset
