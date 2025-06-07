# 📊 Customer Churn Prediction

This repository contains a complete end-to-end machine learning project to predict customer churn using the Telco Customer Churn dataset. It includes detailed **Exploratory Data Analysis (EDA)**, data preprocessing, model training, and evaluation.

---

## 🧾 Dataset

We use the **Telco Customer Churn** dataset, which contains information about customer demographics, services, and whether they churned.

You can download the dataset from: [Kaggle - Telco Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 📌 Project Highlights

### 🔍 Exploratory Data Analysis
- Distribution of target variable (Churn)
- Univariate and bivariate analysis
- Correlation heatmaps
- Visualizations using Seaborn and Matplotlib

### 🧹 Data Preprocessing
- Missing value handling
- Encoding categorical variables with `pd.get_dummies()`
- Feature scaling (optional, not required for Random Forest)

### 🤖 Model Building
- `RandomForestClassifier` from scikit-learn
- Train/test split (80/20)
- Model performance evaluation (accuracy, confusion matrix, classification report)

### 📈 Feature Importance
- Top 10 most important features plotted using bar chart

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
python -m venv venv
source venv/bin/activate  # On Windows use venv\\Scripts\\activate
pip install -r requirements.txt
