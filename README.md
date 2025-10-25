# Bharat Digital Project – Project Samarth

**Project Samarth** is an intelligent Q&A system designed to analyze India’s agriculture and climate datasets, enabling data-driven insights for policymakers and researchers. This prototype demonstrates an end-to-end system that answers complex natural language questions about crop production, rainfall, and policy recommendations.

---

## 🌟 Features

- Compare **average annual rainfall** between two states over the last N years.
- List the **top M most produced crops** by volume in selected states.
- Identify districts with **highest and lowest production** of a specific crop.
- Analyze **crop production trends** and correlate with rainfall data.
- Provide **data-backed policy recommendations** for promoting crops.
- Answers include **source citations** for traceability.

---

## 📂 Datasets

All datasets are stored in the `data/` folder:

| File | Description |
|------|-------------|
| `crop_clean.csv` | Crop production data by State, District, Year, and Crop |
| `rain_clean.csv` | Annual rainfall data by State and Year |

> These datasets were cleaned and simplified for the prototype demo.

---


---

## 🚀 How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/YOUR_USERNAME/Bharat_Digital_Project.git
cd Bharat_Digital_Projec pip install streamlit pandas
t
Open in browser: http://localhost:8501
Try sample questions:
"Compare rainfall and top crop"
"Which district has highest and lowest production"
"Analyze production trend"
"Policy to promote Wheat over Rice"
