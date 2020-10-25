import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

data = [[7, 1], [2, 1], [4, 2], [9, 4], [10, 5], [10, 6], [11, 5], [11, 6], [15, 3], [15, 2], [16, 4], [16, 1]]

df = pd.DataFrame(columns = ['x', 'y'], data = data)

distortions = []

for cluster in range(1, 10):
    km = KMeans(n_clusters=cluster).fit(df[['x', 'y']])

    distance = cdist(df[['x', 'y']], km.cluster_centers_, 'euclidean')

    min_distance = np.min(distance, axis = 1)
    sum_distance = sum(min_distance)

    distortions.append(sum_distance / df[['x', 'y']].shape[0])
plt.plot(range(1, 10), distortions)
plt.show()