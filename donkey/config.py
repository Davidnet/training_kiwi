
import os
import configparser

import donkey as dk

import keras

if int(keras.__version__.split('.')[0]) < 2:
    raise ImportError('You need keras version 2.0.0 or higher. Run "pip install keras --upgrade"')


my_path = os.path.expanduser('~/mydonkey/')
sessions_path = os.path.join(my_path, 'sessions')
models_path = os.path.join(my_path, 'models')
datasets_path = os.path.join(my_path, 'datasets')
results_path = os.path.join(my_path, 'results')
