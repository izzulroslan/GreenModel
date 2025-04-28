import streamlit as st
import random 

st.set_page_config(page_title="About CodeCarbon", layout="centered")

# ✅ Initialize theme state once
if "theme" not in st.session_state:
    st.session_state["theme"] = "Light Mode"

# ✅ Initialize toggle state for UI control (separate from actual theme)
if "toggle_state" not in st.session_state:
    st.session_state["toggle_state"] = (st.session_state["theme"] == "Dark Mode")

# ✅ Handle toggle with rerun to ensure proper state change
new_toggle = st.toggle("Dark Mode 🌙", value=st.session_state["toggle_state"])
if new_toggle != st.session_state["toggle_state"]:
    st.session_state["toggle_state"] = new_toggle
    st.session_state["theme"] = "Dark Mode" if new_toggle else "Light Mode"
    st.rerun()  # 🔁 Force rerun after changing theme

# ✅ Use the updated theme
theme = st.session_state["theme"]

# ✅ Apply the theme CSS
if theme == "Light Mode":
    st.markdown("""
        <style>
        /* Change the top header bar */
        header[data-testid="stHeader"] {
            background-color: #66bb6a;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #e8ebe0;
            color: #000000;
        }
        [data-testid="stSidebar"] {
            background-color: #a5d6a7;
        }
        h1, h2, h3, h4, h5, h6, p, li, span, div {
            color: #343434 !important;
        }
        .stButton>button {
            background-color: #388e3c;
            color: white;
        }
        .stButton>button:hover {
            background-color: #66bb6a;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

# ✅ Main content
st.title("🌿 What is CodeCarbon?")

st.markdown("""
**CodeCarbon** is an **open-source Python package** that estimates the **carbon emissions** produced when running code, especially machine learning or data science code.

Think of it as a **carbon meter** for your AI code — just like a pedometer counts steps, CodeCarbon tracks how much CO₂ your training session is emitting 🌍💻.
""")

st.subheader("🔍 Why is this important?")
st.markdown("""
Because training AI models (especially big ones) uses a lot of electricity. And electricity — depending on the energy source — often generates **carbon emissions**. These emissions contribute to **climate change**.

With **CodeCarbon**, we can:

- **Measure our environmental impact**
- Compare different model setups (e.g., Random Forest vs Logistic Regression)
- Choose **greener configurations** 🌱
- Educate others (like your GreenModel app does!) about the invisible cost of computation
""")

st.subheader("⚙️ How does it work?")
st.markdown("""
1.  **Starts tracking** when you call `tracker.start()`
2.  Tracks:
    - **CPU & GPU usage**
    - **Runtime**
    - **Geographic location** (to estimate the electricity’s CO₂ intensity)
3.  **Stops tracking** when you call `tracker.stop()`
4.  Returns the **CO₂ emissions in kilograms**
5.  Optionally saves it to a `.csv` log file
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