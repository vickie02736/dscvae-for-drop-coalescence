# -*- coding: utf-8 -*-
"""preprocess.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ynW82TeYAyq-4X0MNCCPSFKw3LtecVas
"""

import pandas as pd
from pandas.core.frame import DataFrame

from google.colab import drive
drive.mount('/content/drive')


def mm_normalize(data): 

  normalised_data = (data - data.min())/(data.max() - data.min())

  return normalised_data


class Spliter3: 

  def __init__(self, data, n_test, n_valid, random_state): 

    self.data = data
    self.n_test = n_test
    self.n_valid = n_valid
    self.random_state = random_state

  def split(self): 

    # count
    counter = self.data.iloc[:,[-1]].value_counts()
    # # to dataframe
    # df_result = pd.DataFrame(result)

    # split true / false
    data_true = self.data[self.data.iloc[: , -1] == 1]
    data_false = self.data[self.data.iloc[: , -1] == 0]


    from sklearn.model_selection import train_test_split
    # for data_ture
    features_true = data_true.iloc[:,0:-1]
    Coalescence_true = data_true.iloc[:,[-1]]
    test_size = (self.n_test/2) / data_true.shape[0]
    valid_size = (self.n_valid/2) / (data_true.shape[0] - self.n_test/2)

    X_rem_true, X_test_true, y_rem_true, y_test_true = train_test_split(
        features_true, Coalescence_true, test_size = test_size, random_state = self.random_state)
    X_train_true, X_valid_true, y_train_true, y_valid_true = train_test_split(
        X_rem_true, y_rem_true, test_size = valid_size, random_state = self.random_state)
    data_train_true = pd.concat([X_train_true, y_train_true], axis = 1)
    data_valid_true = pd.concat([X_valid_true, y_valid_true], axis = 1)
    data_test_true = pd.concat([X_test_true, y_test_true], axis = 1)

    # for data_false
    features_false = data_false.iloc[:,0:-1]
    Coalescence_false = data_false.iloc[:,[-1]]
    test_size = (self.n_test/2) / data_false.shape[0]
    valid_size = (self.n_valid/2) / (data_false.shape[0] - self.n_test/2)

    X_rem_false, X_test_false, y_rem_false, y_test_false = train_test_split(
        features_false, Coalescence_false, test_size=test_size, random_state = self.random_state)
    X_train_false, X_valid_false, y_train_false, y_valid_false = train_test_split(
        X_rem_false, y_rem_false, test_size = valid_size, random_state = self.random_state)
    
    data_train_false = pd.concat([X_train_false, y_train_false], axis = 1)
    data_valid_false = pd.concat([X_valid_false, y_valid_false], axis = 1)
    data_test_false = pd.concat([X_test_false, y_test_false], axis = 1)


    # true_false_concat
    self.data_train = pd.concat([data_train_true, data_train_false], axis = 0)
    self.data_valid = pd.concat([data_valid_true, data_valid_false], axis = 0)
    self.data_test = pd.concat([data_test_true, data_test_false], axis = 0)

    from sklearn.utils import shuffle
    self.data_train = shuffle(self.data_train, random_state = 0)
    self.data_valid = shuffle(self.data_valid, random_state = 0)
    self.data_test = shuffle(self.data_test, random_state = 0)

  def data_train(self):
    return self.data_train

  def data_valid(self):
    return self.data_valid
  
  def data_test(self):
    return self.data_test
    
  def counter(self):  
    return self.counter