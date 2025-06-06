import streamlit as st
import random
from theme import apply_theme 

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
if theme != st.session_state["theme"]:
    st.session_state["theme"] = theme
    st.rerun()  # 🔁 Force rerun immediately

# Apply theme based on selected
apply_theme()

st.title("🌱 Welcome to GreenModel")

st.markdown("""
Welcome to **GreenModel: AI Carbon Emission Tracker**!  
            
GreenModel is a user-friendly Streamlit platform that helps users train machine learning models while 
tracking their carbon emissions in real time. It promotes sustainable AI development by 
using the CodeCarbon library to measure and visualize the environmental impact of model training. 
The platform also includes educational sections about carbon emissions, a global CO₂ dashboard, and 
an AI chatbot that tracks the emissions generated by chat interactions.
            
---

### 🔍 What You Can Explore:
    
- 📘 **Carbon Emission Information**  
    Learn about carbon dioxide emissions, their impact, and how we can reduce them.
            
- ♻️ **CodeCarbon Information**  
    Understand how CodeCarbon works and its role in tracking emissions.
            
- 🌍 **Global CO₂ Emissions Dashboard**  
    Visualize emissions data across countries with interactive graphs and charts.

- 🧠 **ML Model Training Carbon Emission Tracker**  
    Train and evaluate models, track their CO₂ emissions in real time.            

- 🤖 **Chatbot Carbon Emission Tracker**  
    Chat with an OpenAI-powered assistant, and track the CO₂ emissions generated per response.  
    Use the 🌳 Green Mode toggle in the sidebar to switch between high-efficiency (lower emissions) and creative (higher emissions) model settings.

---

### 🌟 About GreenModel
- ✅ Measures real-world carbon footprint of AI models
- ✅ Powered by [CodeCarbon](https://mlco2.github.io/codecarbon/)
- ✅ Encourages sustainable and responsible AI development
- ✅ Promotes awareness of digital carbon footprints
- ✅ Educates users on the environmental cost of computation
---

### 📣 Spread Awareness & Educate Others

GreenModel is more than just a tool — it's a platform for **raising awareness** about the environmental impact of AI.  
Whether you're a student, developer, researcher, or just curious, use this app to **explore**, **learn**, and **inspire others** to build a greener future in tech.
            
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
