# ⚽ Footballer Stats EDA

This project performs **Exploratory Data Analysis (EDA)** on a dataset containing footballer performance statistics from various leagues and years. The goal is to uncover insights into player efficiency, league trends, and scoring patterns.

---

## 📁 Dataset

- **Source**: Provided CSV file (`Data.csv`)
- **Size**: 660 rows × 15 columns
- **Fields include**:
  - Player name, country, club, and league
  - Matches played, minutes, goals, expected goals (xG)
  - Shooting stats (shots, on-target shots)
  - Year of observation

---

## 🧪 Analysis Goals

- Understand top-performing players
- Compare actual goals vs expected goals (xG)
- Analyze scoring efficiency by league and year
- Visualize trends over time for players (e.g., Lionel Messi)
- Identify league-wide scoring patterns

---

## 📊 Key Visualizations

- Goals over time for selected players
- Top 10 scorers by total goals
- Average goals per league per year
- Distribution of player performance metrics
- Correlation heatmap of numerical features

---

## 📌 Key Insights

- Lionel Messi peaked in 2016 and 2018 with 30+ goals.
- Some players consistently over/underperform their xG.
- Leagues show varying attacking tendencies over years.
- A dip in goals is observed in 2020, possibly due to fewer matches.

---

## 📦 Requirements

To run the notebook, install the following Python packages:

```bash
pip install pandas matplotlib seaborn jupyter
