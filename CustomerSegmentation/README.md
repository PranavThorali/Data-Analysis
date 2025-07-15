# 🧠 Customer Segmentation Using RFM and Clustering

Done by Pranav Thorali

This project performs customer segmentation using Recency, Frequency, and Monetary (RFM) analysis on a real-world e-commerce dataset. It applies multiple clustering algorithms like KMeans, Hierarchical Clustering, and DBSCAN to uncover actionable customer groups for targeted marketing.

---

## 📦 Dataset
- **Source:** UCI Online Retail Dataset
- **Records:** ~500,000 transactions
- **Features Used:** InvoiceDate, Quantity, UnitPrice, CustomerID

---

## 📊 Techniques Used
- **RFM Feature Engineering**
- **Log Transform + Standard Scaling**
- **Clustering Algorithms:**
  - KMeans (with Elbow Method)
  - Hierarchical Clustering (Dendrogram)
  - DBSCAN (density-based)
- **Visualization:**
  - PCA (2D projection)
  - Seaborn/Matplotlib cluster plots

  ## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/customer-segmentation-rfm.git
cd customer-segmentation-rfm
```

### 2. Create environment & install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Jupyter Notebooks
```bash
jupyter notebook
```

Explore the workflow in:
- `notebooks/01_eda.ipynb`
- `notebooks/02_rfm_feature_eng.ipynb`
- `notebooks/03_clustering.ipynb`

## 🧱 Project Structure

```
customer-segmentation-rfm/
├── data/                    # Raw and processed data
├── notebooks/              # EDA, RFM, and clustering notebooks
├── src/                    # Python scripts for full pipeline
├── app/                    # Streamlit UI (optional)
├── reports/                # Summary insights and visual output
├── requirements.txt        # Python dependencies
├── README.md               # Project overview and usage
└── .gitignore              # Files/folders to ignore in git
```
