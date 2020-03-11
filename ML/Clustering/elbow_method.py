# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:13:31 2020

@author: Luna
"""

from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1,11, size=(2,20))
#plt.plot()
#plt.xlim([0, 11])
#plt.ylim([0, 11])
#plt.title('Dataset')
#plt.scatter(data[0,:], data[1,:])
#plt.show()

# k means determine k
distortions = []
K = np.arange(1,20)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(np.transpose(data))
    kmeanModel.fit(np.transpose(data))
    distortions.append(sum(np.min(cdist(np.transpose(data), kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / np.transpose(data).shape[0])
    
#Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()
