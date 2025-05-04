import streamlit as st
import pandas as pd
import plotly.express as px
import random
from theme import apply_theme

st.set_page_config(page_title="Global CO₂ Emissions", layout="centered")

apply_theme()

st.title("🌍 Global CO₂ Emissions Dashboard")

with st.expander("📖 Global CO₂ Emissions Dashboard User Guide and Data Source"):
    st.markdown("""
    ## ℹ️ User Guide

    ### 1. How to Use
    - **Select a country** to see its emissions trend.
    - **View the Top 10 Emitters** for the latest year.

    ### 2. Data Source
    [Our World in Data - CO₂ and Greenhouse Gas Emissions](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions)
    - Annual emissions by country (million tonnes)
    - Years: 2000-2022
    
    ---

     **📝 Notes:** Some countries might have limited data. Knowledge leads to action.
    """)
    
@st.cache_data
def load_data():
    df = pd.read_csv("data/countries_co2_data.csv")
    df = df[df["year"] >= 2000]
    df = df[~df["country"].isin(["World", "Asia", "Europe", "Africa", "North America", "South America", "European Union", "Oceania"])]
    return df

df = load_data()

countries = df["country"].unique()
selected_country = st.selectbox("Select a country:", sorted(countries), index=None, placeholder="Select the country .." )

country_data = df[df["country"] == selected_country]

st.subheader(f"CO₂ Emissions Over Time for {selected_country}")
fig = px.line(country_data, x="year", y="co2", labels={"co2": "CO₂ (million tonnes)"}, title=f"{selected_country} - CO₂ Emissions (2000-2022)")
st.plotly_chart(fig, use_container_width=True)

if not country_data.empty:
    total_emissions = country_data["co2"].sum()
    st.info(f"🌟 Since 2000, {selected_country} emitted approximately **{total_emissions:,.0f} million tonnes** of CO₂.")
    st.markdown("""
    **Fun Fact:**  
    - 1 million tonnes of CO₂ is roughly equal to the emissions from **217,000 cars** running for an entire year 🚗.
    - Imagine **building 1,000 skyscrapers** — that's the kind of energy we're talking about! 🏙️
    ---
    """)

st.subheader("🌎 Top 10 Countries by CO₂ Emissions (Latest Year)")
latest_year = df["year"].max()
top10 = df[df["year"] == latest_year].sort_values(by="co2", ascending=False).head(10)
fig2 = px.bar(top10, x="country", y="co2", labels={"co2": "CO₂ (million tonnes)"}, title=f"Top 10 Emitters in {latest_year}")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
**🏆 Why Top Emitters Matter?**
- Understanding the biggest contributors helps focus global efforts on climate solutions.  
- Together, the top 10 countries produce about 65%-70% of all global CO₂ emissions!
---
""")

st.success("""
### 🌱 Did You Know?
If the world emits **1 billion tonnes** of CO₂:
- It would take **45 billion trees** 🌳 a whole year to absorb it.
- Or it's like **2 billion people** flying from New York to London ✈️ at once!

Every step toward emission reduction matters. 💚
""")

# List of "Did You Know?" fun facts
did_you_know_facts = [
    "🌱 It would take 45 billion trees 🌳 a whole year to absorb 1 billion tonnes of CO₂!",
    "✈️ 1 billion people flying from New York to London equals 500 millions tonnes of CO₂!",
    "🌍 The average car emits about 4.6 metric tonnes of CO₂ per year.",
    "🏡 Heating and cooling buildings accounts for about 50% of global energy use.",
]

# List of eco-friendly tips
eco_tips = [
    "💡 Switch off lights and electronics when not in use.",
    "🚴‍♂️ Walk, cycle, or carpool whenever possible.",
    "♻️ Reduce, Reuse, and Recycle — the 3 magic R's!",
    "🍃 Compost food scraps to reduce landfill emissions.",
    "🛒 Bring your own reusable bag when shopping.",
    "💧 Fix leaking taps to save thousands of liters of water yearly.",
    "🥦 Choose more plant-based meals to lower your carbon footprint.",
    "🔋 Use rechargeable batteries whenever possible.",
]

# Randomly decide whether to show a fact or a tip
category = random.choice(["fact", "tip"])

# Define the opening word based on category
if category == "fact":
    random_message = random.choice(did_you_know_facts)
    opening_word = "🌍 **Did You Know?**"
else:
    random_message = random.choice(eco_tips)
    opening_word = "🌿 **Green Tip of the Day:**"

# Display the message with the opening word in the sidebar
with st.sidebar:
    st.info(f"{opening_word}\n\n{random_message}")
