# Bharat Digital Project – Project Samarth

**Project Samarth** is an intelligent Q&A system that integrates agricultural and climate datasets from India to provide **data-driven insights**. This prototype demonstrates an end-to-end workflow for analyzing crop production, rainfall trends, and policy recommendations, using Python, Pandas, and Streamlit.

---

## 🖥️ Project Overview

The system allows users to ask **natural language questions** and get **quantitative, traceable answers**. It combines multiple datasets, performs aggregation and correlation analysis, and presents results interactively through a web interface.

---

## 🌟 Features

- Compare **average annual rainfall** between two states over the last N years.  
- List the **top M most produced crops** by volume in selected states.  
- Identify districts with **highest and lowest production** of a specific crop.  
- Analyze **crop production trends** and correlate with rainfall data.  
- Provide **data-backed policy recommendations** for promoting crops.  
- Include **source citations** for each answer for traceability.  

---

## 📂 Datasets

| File | Description |
|------|-------------|
| `crop_clean.csv` | Crop production data by State, District, Year, and Crop |
| `rain_clean.csv` | Annual rainfall data by State and Year |

> Stored in the `data/` folder. Datasets are cleaned and structured for real-time querying.

---

## ⚙️ Technical Stack

- Python 3.x  
- Pandas – Data cleaning & aggregation  
- Streamlit – Interactive web Q&A interface  
- CSV – Structured datasets  

---

## 🔍 Methodology

### Step 2: Load Datasets

```python
import pandas as pd

crop_df = pd.read_csv("data/crop_clean.csv")
rain_df = pd.read_csv("data/rain_clean.csv")

crop_df.fillna(0, inplace=True)
rain_df.fillna(0, inplace=True)
Step 3: Define Q&A Functions
Functions map user questions to dataset queries, e.g.,
Rainfall comparison & top crops
District production analysis
Production trend & correlation
Policy recommendations
Step 4: Build Streamlit Interface
import streamlit as st

st.title("Project Samarth - Agriculture & Climate Q&A")

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    # Map keywords to functions
    if "rainfall" in question.lower():
        result = rainfall_and_top_crops("Maharashtra", "Gujarat", "Wheat")
    st.write(result)
🚀 How to Run
Install dependencies:
pip install streamlit pandas
Run the Streamlit app:
streamlit run app.py
Open in browser: http://localhost:8501
Try sample questions:
"Compare rainfall and top crop"
"Which district has highest and lowest production"
"Analyze production trend"
"Policy to promote Wheat over Rice"
