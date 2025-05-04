import streamlit as st
import random
from theme import apply_theme  # ⬅️ import the theme function

# ✅ Set page config FIRST
st.set_page_config(page_title="GreenModel: Home", layout="centered")

# Step 1: Initialize default theme in session state if not set
if "theme" not in st.session_state:
    st.session_state["theme"] = "Light Mode"  # default

# Step 2: Radio button uses current session value as default
theme = st.radio(
    "🌓 Choose Theme:",
    ("Light Mode", "Dark Mode"),
    index=0 if st.session_state["theme"] == "Light Mode" else 1
)

# Step 3: Update session state if user changed theme
st.session_state["theme"] = theme

# Apply theme based on selected
apply_theme()

st.title("🌱 Welcome to GreenModel")

st.markdown("""
Welcome to **GreenModel: AI Carbon Emission Tracker**!  
This platform empowers you to **train machine learning models** while keeping track of **carbon emissions**.

---

### 🔍 What You Can Explore:
    
- 📘 **Carbon Emission Information**  
    Learn about carbon dioxide emissions, their impact, and how we can reduce them.
            
- ♻️ **CodeCarbon Information**  
    Understand how CodeCarbon works and its role in tracking emissions.
            
- 🌍 **Global CO₂ Emissions Dashboard**  
    Visualize emissions data across countries with interactive graphs and charts.

- 🧠 **GreenModel Tracker**  
    Train and evaluate models, track their CO₂ emissions in real time.            

- 🤖 **Chatbot Carbon Emission**
    Chatbot powered by OpenAI that also tracks the carbon emissions of each chat interaction.

---

### 🌟 About GreenModel
- ✅ Measures real-world carbon footprint of AI models
- ✅ Powered by [CodeCarbon](https://mlco2.github.io/codecarbon/)
- ✅ Promotes greener, more sustainable AI practices

---

Made with ❤️ by [Izzul Roslan](https://github.com/izzulroslan)
""")

# List of "Did You Know?" fun facts
did_you_know_facts = [
    "🌱 It would take 45 trillion trees 🌳 a whole year to absorb 1 billion tonnes of CO₂!",
    "✈️ 1 billion people flying from New York to London equals 500 million tonnes of CO₂!",
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
