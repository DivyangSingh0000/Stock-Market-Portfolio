# 📈 Stock Market Portfolio Analysis with Python

![Last Commit](https://img.shields.io/github/last-commit/DivyangSingh0000/Stock-Market-Portfolio)
![Issues](https://img.shields.io/github/issues/DivyangSingh0000/Stock-Market-Portfolio)
![Stars](https://img.shields.io/github/stars/DivyangSingh0000/Stock-Market-Portfolio?style=social)

A comprehensive data analysis project focused on stock market portfolio trends and predictions using Python. The project leverages real-time data, sentiment analysis, technical indicators, and machine learning models to provide insights into market behavior.

---

## 📊 Key Features

- 📥 **Data Collection** using `yfinance` and `requests`
- 🧼 **Data Cleaning & Preprocessing** using `pandas`, `sklearn.preprocessing`
- 📈 **Visualizations** with `matplotlib` and `seaborn`
- 💬 **Sentiment Analysis** on news headlines using `vaderSentiment`
- 🧠 **Machine Learning Models** with `sklearn.ensemble` and `sklearn.model_selection`
- 📉 **Model Evaluation** using `sklearn.metrics`

---

## 🧪 Libraries Used

- `yfinance` – Fetch historical stock data
- `pandas` – Data wrangling and manipulation
- `matplotlib.pyplot` & `seaborn` – Visualization and trend plotting
- `requests` – Fetching external API/news data
- `vaderSentiment.vaderSentiment` – Sentiment analysis on news headlines or tweets
- `sklearn.ensemble` – Machine learning (Random Forest, Gradient Boosting)
- `sklearn.model_selection` – Train-test split and cross-validation
- `sklearn.metrics` – Performance metrics (Accuracy, Confusion Matrix, etc.)
- `sklearn.preprocessing` – Feature scaling, encoding

---

## 📁 Project Structure

```bash
.
├── data/                     # CSVs and raw data
├── notebooks/                # Jupyter notebooks for EDA and modeling
├── src/
│   ├── data_collection.py    # Script for yfinance + requests API
│   ├── sentiment_analysis.py # Sentiment processing with VADER
│   ├── visualizations.py     # Charts and plots
│   ├── model_train.py        # ML training scripts
│   └── utils.py              # Helper functions
├── requirements.txt
├── README.md
└── main.py                   # Main pipeline script
