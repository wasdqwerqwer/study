import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns


df = pd.read_csv('fruit_data_with_colors.csv')
sns.lmplot('fruit_label', 'fruit_name', 'fruit_subtype', 'mass', 'width', 'height', 'color_score', data = df, hue= 'STATUS', fit_reg = False)

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

shwo()