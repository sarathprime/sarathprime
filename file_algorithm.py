
# importing the libraries
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split as tts
import seaborn as sns
import matplotlib.pyplot as plt




data = pd.read_csv('bdata.csv', sep='|')

data.head()