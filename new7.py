import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


df =pd.read_csv('cluster_sample_1.csv')
#plt.scatter(df[['x']], df[['y']])

distortions = []

for cluster in range(1, 20):
    km = KMeans(n_clusters=cluster).fit(df[['x', 'y']])

    distance = cdist(df[['x', 'y']], km.cluster_centers_, 'euclidean')

    min_distance = np.min(distance, axis = 1)
    sum_distance = sum(min_distance)

    distortions.append(sum_distance / df[['x', 'y']].shape[0])
plt.plot(range(1, 20), distortions)

plt.show()

