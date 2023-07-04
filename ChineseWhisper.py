import numpy as np

import sys
import pandas as pd
import plotly.express as px
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
def cluster_(data,num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(data)
    labels = kmeans.labels_
    pca = PCA(n_components=3)
    data_pca = pca.fit_transform(data)
    df = pd.DataFrame(data_pca, columns=[f"PC-{i+1}" for i in range(3)])
    df['Cluster'] = labels
    fig = px.scatter_3d(df, x='PC-1', y='PC-2', z='PC-3', color='Cluster', title="3D Clustering Visualization")
    fig.show()
    return df
def cluster(vectors_weight,data,num_clusters):
    data_=np.zeros([len(data),len(vectors_weight)])
    for i in range(len(data)):
        for j in range(len(vectors_weight)):
            data_[i,j]=vectors_weight[j]["weight"]*data[i,j]
    return cluster_(data_,num_clusters)