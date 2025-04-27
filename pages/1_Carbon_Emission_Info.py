import streamlit as st
import random 

st.set_page_config(page_title="About Carbon Emission", layout="centered")

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
    
st.title("🌍 About Carbon Emissions and Why It Matters")

st.header("What Are Carbon Emissions?")
st.write("""
Carbon emissions, mainly carbon dioxide (CO₂), are gases released when fossil fuels like coal, oil, and gas are burned.
These gases trap heat in the atmosphere, leading to global warming and climate change.
""")

st.header("Where Do Carbon Emissions Come From?")
st.markdown("""
- 🚗 **Transportation**: Cars, trucks, and airplanes burning fuel.
- ⚡ **Electricity Production**: Power plants using coal and gas.
- 🏭 **Industry**: Manufacturing materials like steel and cement.
- 🌾 **Agriculture**: Farming activities and livestock.
- 🏠 **Residential**: Heating, cooling, and powering homes.
""")

st.header("Impact of Carbon Emissions")
st.markdown("""
- 🔥 Rising global temperatures
- 🌪️ More extreme weather events
- 🌊 Melting ice caps and rising sea levels
- 🐾 Threats to wildlife and ecosystems
- 🏥 Increased health risks
""")

st.header("Carbon Emissions from Technology")
st.write("""
Digital technologies such as data centers, cloud computing, and streaming services consume large amounts of energy. 
The ICT sector could contribute up to 14% of global emissions by 2040 if unchecked.
""")

st.header("Carbon Emissions in AI and Machine Learning")
st.write("""
Training AI models requires high computational power, often leading to significant CO₂ emissions.
Large models, in particular, can emit hundreds of tons of CO₂ during training.
Even smaller models can have an impact when trained at scale.
""")

st.header("How Can We Reduce Carbon Emissions?")
st.markdown("""
- 🌳 **Use Renewable Energy**  
  Switch to energy sources like solar, wind, and hydro instead of fossil fuels.
  
- 🚴 **Promote Sustainable Transportation**  
  Walk, cycle, carpool, or use electric vehicles whenever possible.
  
- 🏡 **Improve Energy Efficiency**  
  Upgrade appliances, insulate homes, and use smart energy systems to reduce waste.
  
- 🌱 **Adopt Greener Technologies**  
  Train AI models more efficiently, use greener cloud providers, and optimize code to consume less power.
  
- 🍴 **Make Sustainable Choices**  
  Reduce meat consumption, waste less food, and support eco-friendly companies.
  
- 📚 **Raise Awareness and Educate Others**  
  Share knowledge about the importance of carbon reduction in both technology and daily life.
""")

st.header("How GreenModel Helps 🌿")
st.write("""
GreenModel monitors and tracks the carbon footprint during model training. 
It recommends greener alternatives to reduce emissions while maintaining high performance.
Together, we can build smarter and greener AI systems.
""")

st.success("🌱 Every choice matters. Let's create technology that cares for our planet!")

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