import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# 设置维度和聚类数量
dimensions = 4
num_clusters = 4

# 生成随机 N-维数据
data, _ = make_blobs(n_samples=500, centers=num_clusters, n_features=dimensions, random_state=42)

# 执行 K-means 聚类
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data)
labels = kmeans.labels_

# 应用PCA将N维数据投影到3D空间以进行可视化
pca = PCA(n_components=3)
data_pca = pca.fit_transform(data)

# 创建一个用于可视化的 DataFrame
df = pd.DataFrame(data_pca, columns=[f"PC-{i+1}" for i in range(3)])
df['Cluster'] = labels
# 将聚类结果可视化
fig = px.scatter_3d(df, x='PC-1', y='PC-2', z='PC-3', color='Cluster', title="3D 聚类可视化")
fig.show()
