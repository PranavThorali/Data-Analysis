import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy.cluster.hierarchy import dendrogram, linkage

def load_data(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    df = df[df['CustomerID'].notnull()]
    return df

### rfm feature engineering
def calculate_rfm(df):
    ref_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (ref_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalAmount': 'sum'
    }).rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalAmount': 'Monetary'
    })
    return rfm

### data preprocessing
def preprocess_rfm(rfm):
    rfm_log = np.log1p(rfm)
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_log)
    return rfm_scaled, rfm_log

### kmeans clustering
def kmeans_clustering(data, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    return kmeans.fit_predict(data)

### agglomerative clustering
def agglomerative_clustering(data, n_clusters=4):
    model = AgglomerativeClustering(n_clusters=n_clusters)
    return model.fit_predict(data)

### dbscan
def dbscan_clustering(data, eps=0.7, min_samples=5):
    model = DBSCAN(eps=eps, min_samples=min_samples)
    return model.fit_predict(data)

### dimensionality reduction for visualization
def reduce_dimensions(data, method='tsne'):
    if method == 'pca':
        pca = PCA(n_components=2)
        return pca.fit_transform(data)
    else:
        tsne = TSNE(n_components=2, perplexity=30, random_state=42)
        return tsne.fit_transform(data)

### dendrogram for agglomerative clustering
def plot_dendrogram(data):
    Z = linkage(data, method='ward')
    plt.figure(figsize=(10, 5))
    dendrogram(Z)
    plt.title('Customer Dendrogram')
    plt.xlabel('Customer Index')
    plt.ylabel('Distance')
    plt.show()

### visualize clusters
def plot_clusters(embedded_data, labels):
    df_vis = pd.DataFrame(embedded_data, columns=['X', 'Y'])
    df_vis['Cluster'] = labels
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df_vis, x='X', y='Y', hue='Cluster', palette='Set2')
    plt.title('Customer Segments')
    plt.show()

### main function
def main():
    df = load_data("data/online_retail.csv")
    rfm = calculate_rfm(df)
    rfm_scaled, rfm_log = preprocess_rfm(rfm)

    # Choose Clustering
    cluster_labels = kmeans_clustering(rfm_scaled, n_clusters=4)
    # cluster_labels = agglomerative_clustering(rfm_scaled, n_clusters=4)
    # cluster_labels = dbscan_clustering(rfm_scaled, eps=0.7)

    rfm['Cluster'] = cluster_labels
    print(rfm.groupby('Cluster').mean())

    # Visualize
    embedded_data = reduce_dimensions(rfm_scaled, method='tsne')
    plot_clusters(embedded_data, cluster_labels)

    # Optional dendrogram
    # plot_dendrogram(rfm_scaled)

if __name__ == "__main__":
    main()
