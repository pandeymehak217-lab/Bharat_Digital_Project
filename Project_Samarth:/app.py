import pandas as pd
import os
import streamlit as st

# ------------------------------
# Step 1: Create data folder & CSVs
# ------------------------------
os.makedirs("data", exist_ok=True)

# Crop data
crop_data = {
    "State": ["Maharashtra","Maharashtra","Gujarat","Gujarat",
              "Maharashtra","Maharashtra","Gujarat","Gujarat"],
    "District": ["Pune","Nashik","Ahmedabad","Surat",
                 "Pune","Nashik","Ahmedabad","Surat"],
    "Year": [2022,2022,2022,2022,2021,2021,2021,2021],
    "Crop": ["Wheat","Wheat","Wheat","Wheat","Wheat","Wheat","Wheat","Wheat"],
    "Production": [1200,900,800,700,1100,950,850,720]
}
crop_df = pd.DataFrame(crop_data)
crop_df.to_csv("data/crop_clean.csv", index=False)

# Rainfall data
rain_data = {
    "State": ["Maharashtra","Maharashtra","Maharashtra","Gujarat","Gujarat","Gujarat"],
    "Year": [2022,2021,2020,2022,2021,2020],
    "Rainfall_mm": [1023,980,1010,890,870,860]
}
rain_df = pd.DataFrame(rain_data)
rain_df.to_csv("data/rain_clean.csv", index=False)

# ------------------------------
# Step 2: Load datasets
# ------------------------------
crop_df = pd.read_csv("data/crop_clean.csv")
rain_df = pd.read_csv("data/rain_clean.csv")

# ------------------------------
# Step 3: Functions for Q&A
# ------------------------------

def rainfall_and_top_crops(state_x, state_y, crop_type, years=2, top_m=2):
    rain_x = rain_df[rain_df['State'] == state_x].tail(years)
    rain_y = rain_df[rain_df['State'] == state_y].tail(years)
    avg_x = rain_x['Rainfall_mm'].mean()
    avg_y = rain_y['Rainfall_mm'].mean()
    
    crops_x = crop_df[(crop_df['State'] == state_x) & (crop_df['Crop'] == crop_type) & (crop_df['Year'].isin(rain_x['Year']))]
    crops_y = crop_df[(crop_df['State'] == state_y) & (crop_df['Crop'] == crop_type) & (crop_df['Year'].isin(rain_y['Year']))]
    
    top_crops_x = crops_x.groupby('Crop')['Production'].sum().sort_values(ascending=False).head(top_m)
    top_crops_y = crops_y.groupby('Crop')['Production'].sum().sort_values(ascending=False).head(top_m)
    
    return f"""
Average Rainfall ({years} years):
{state_x}: {avg_x:.1f} mm, {state_y}: {avg_y:.1f} mm (Source: IMD dataset)

Top {top_m} crops of {crop_type}:
{state_x}: {top_crops_x.to_dict()} (Source: Agriculture dataset)
{state_y}: {top_crops_y.to_dict()} (Source: Agriculture dataset)
"""

def compare_districts(state_x, state_y, crop_name):
    latest_year = crop_df['Year'].max()
    
    df_x = crop_df[(crop_df['State']==state_x) & (crop_df['Crop']==crop_name) & (crop_df['Year']==latest_year)]
    df_y = crop_df[(crop_df['State']==state_y) & (crop_df['Crop']==crop_name) & (crop_df['Year']==latest_year)]
    
    top_x = df_x.loc[df_x['Production'].idxmax()]
    low_y = df_y.loc[df_y['Production'].idxmin()]
    
    return f"""
{state_x} top district for {crop_name} in {latest_year}: {top_x['District']} ({top_x['Production']} tonnes)
{state_y} lowest district for {crop_name} in {latest_year}: {low_y['District']} ({low_y['Production']} tonnes)
"""

def production_trend_with_rain(region, crop_name, years=3):
    latest_year = crop_df['Year'].max()
    year_range = list(range(latest_year-years+1, latest_year+1))
    
    crop_data_region = crop_df[(crop_df['State']==region) & (crop_df['Crop']==crop_name) & (crop_df['Year'].isin(year_range))]
    rain_data_region = rain_df[(rain_df['State']==region) & (rain_df['Year'].isin(year_range))]
    
    merged = pd.merge(crop_data_region.groupby('Year')['Production'].sum().reset_index(),
                      rain_data_region[['Year','Rainfall_mm']], on='Year')
    
    corr = merged['Production'].corr(merged['Rainfall_mm'])
    
    return f"Correlation between {crop_name} production and rainfall in {region} over last {years} years: {corr:.2f} (Source: Agriculture + IMD datasets)"

def policy_arguments(region, crop_a, crop_b, years=2):
    latest_year = crop_df['Year'].max()
    year_range = list(range(latest_year-years+1, latest_year+1))
    
    data_a = crop_df[(crop_df['State']==region) & (crop_df['Crop']==crop_a) & (crop_df['Year'].isin(year_range))]
    data_b = crop_df[(crop_df['State']==region) & (crop_df['Crop']==crop_b) & (crop_df['Year'].isin(year_range))]
    
    rain = rain_df[(rain_df['State']==region) & (rain_df['Year'].isin(year_range))]
    
    arg1 = f"{crop_a} has higher average production ({data_a['Production'].mean():.1f} tonnes) vs {crop_b} ({data_b['Production'].mean():.1f})"
    arg2 = f"{crop_a} is more resilient to rainfall variation (correlation: {data_a['Production'].corr(rain['Rainfall_mm']):.2f})"
    arg3 = f"{crop_a} has more stable year-to-year production (std dev: {data_a['Production'].std():.1f}) vs {crop_b} ({data_b['Production'].std():.1f})"
    
    return f"Arguments for promoting {crop_a} over {crop_b} in {region}:\n1. {arg1}\n2. {arg2}\n3. {arg3}\n(Source: Agriculture + IMD datasets)"

# ------------------------------
# Step 4: Streamlit Interface
# ------------------------------
st.title("Project Samarth - Agriculture & Climate Q&A")

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    q = question.lower()
    if "rainfall" in q and "top crop" in q:
        result = rainfall_and_top_crops("Maharashtra", "Gujarat", "Wheat", years=2, top_m=2)
    elif "highest" in q or "lowest" in q:
        result = compare_districts("Maharashtra", "Gujarat", "Wheat")
    elif "trend" in q or "correlate" in q:
        result = production_trend_with_rain("Maharashtra", "Wheat", years=3)
    elif "policy" in q or "promote" in q:
        result = policy_arguments("Maharashtra", "Wheat", "Rice", years=2)
    else:
        result = "Demo system currently answers rainfall, top crops, production trend, and policy questions only."
    
    st.write(result)
