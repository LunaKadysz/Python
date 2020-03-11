# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:27:21 2019

@author: Luna Kadysz
"""

from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=5, random_state=50)
points = data[0]

plt.figure()
plt.scatter(data[0][:,0], data[0][:,1], c=data[1], cmap='viridis')
plt.xlim(-15,15)
plt.ylim(-15,15)

kmeans = KMeans(n_clusters=4)
kmeans.fit(points)
print(kmeans.cluster_centers_)

y_km = kmeans.fit_predict(points)

plt.figure()
plt.scatter(points[y_km ==0,0], points[y_km == 0,1], s=100, c='red')
plt.scatter(points[y_km ==1,0], points[y_km == 1,1], s=100, c='black')
plt.scatter(points[y_km ==2,0], points[y_km == 2,1], s=100, c='blue')
plt.scatter(points[y_km ==3,0], points[y_km == 3,1], s=100, c='cyan')