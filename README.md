# 📊 Python Frameworks Assignment -- CORD-19 Dataset

## 📌 Project Overview

This project focuses on analyzing the **CORD-19 (COVID-19 Open Research
Dataset)** and presenting insights through a **Streamlit web
application**. The goal is to practice real-world data analysis,
cleaning, visualization, and dashboard development.

---

## 🎯 Learning Objectives

- Import and explore real-world datasets.\
- Handle and clean missing or inconsistent data.\
- Generate meaningful visualizations (trends, distributions, word
  clouds).\
- Build an **interactive dashboard** using **Streamlit**.

---

## 🔑 Key Steps Implemented

1.  **Data Loading**
    - Imported `metadata.csv`.\
    - Inspected structure and basic statistics.
2.  **Data Cleaning**
    - Handled missing values.\
    - Converted date columns to datetime format.\
    - Created new derived features for analysis.
3.  **Data Analysis**
    - Publications by year.\
    - Top journals and sources.\
    - Frequent keywords/words in abstracts.
4.  **Visualization**
    - Bar charts for yearly publications and top journals.\
    - Word cloud for frequent terms.
5.  **Streamlit Dashboard**
    - Interactive filters (year, journal).\
    - Dynamic charts and visualizations.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Abigail-Addo/Frameworks_Assignment.git
cd Frameworks_Assignment/app
```

### 2. Download the Dataset

Download **metadata.csv** from Kaggle:\
👉 [CORD-19 Research Challenge
Dataset](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv)

Place the file inside the **`data/`** folder of this project, replacing
the existing file if necessary.

---

## 🚀 Running the Project

### Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

This will start a local server, and the dashboard will be available in
your browser (default: `http://localhost:8501`).

---

### Run the Jupyter Notebook

Open the **`cord19_analysis.ipynb`** file in Jupyter Notebook or
JupyterLab:

```bash
jupyter notebook cord19_analysis.ipynb
```

This notebook walks through the entire analysis process step by step.

---
