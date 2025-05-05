
import streamlit as st
from codecarbon import EmissionsTracker
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import time
import plotly.express as px
import random
from theme import apply_theme

# Streamlit config
st.set_page_config(page_title="GreenModel: Carbon Tracker", layout="centered")

apply_theme()

st.title("🌱 ML Model Training Carbon Emission Tracker")

with st.expander("📖 ML Model Training Carbon Emission Tracker User Guide"):
    st.markdown("""
    **ℹ️ User Guide**
                
    **1. Choose a Dataset**
                
    Select from `Iris`, `Wine`, or `Breast Cancer` datasets. These are classic machine learning datasets used for classification tasks.

    **2. Choose a Model**
                
    Pick between:
    - `Random Forest`: A tree-based ensemble model.
    - `Logistic Regression`: A simple linear model for classification.

    **3. Set Parameters**
                
    Adjust:
    - `Number of Trees` for Random Forest  
    - `Max Iterations` for Logistic Regression  

    **4. Train & Track**
                
    Click **Train Model & Track Emissions** to:
    - Train the selected model on the dataset
    - Measure CO₂ emissions using CodeCarbon
    - See the model’s accuracy and emissions (in grams)

    **📈 Additional Insights**

    - **Previous Runs Table**: Shows accuracy & CO₂ for all your training runs.
    - **Emissions Chart**: Visualizes emissions from each run.
    - **Greenest Configuration**: Highlights the most eco-friendly model setup for each dataset.
    - **Real-world Equivalents**: Understand your emissions in terms of real-life activities (e.g., candles burned, meters driven).

    ---

    💡 **Tip:** Try different models and parameters to see which is the most energy-efficient!
    """)
    
# Session state logs
if "logs" not in st.session_state:
    st.session_state.logs = []

st.markdown("### 📊 Choose a dataset")
dataset_name = st.radio("Dataset", ["Iris", "Wine", "Breast Cancer"])

st.markdown("### 🧠 Choose a model")
model_type = st.radio("Model", ["Random Forest", "Logistic Regression"])

# Parameters input
if model_type == "Random Forest":
    n_estimators = st.slider("🌲 Number of Trees", 10, 200, 100, 10)
else:
    max_iter = st.slider("🔁 Max Iterations (Epochs)", 50, 500, 100, 50)

# Load dataset
def load_data(name):
    if name == "Iris":
        data = load_iris()
    elif name == "Wine":
        data = load_wine()
    elif name == "Breast Cancer":
        data = load_breast_cancer()
    return data.data, data.target

X, y = load_data(dataset_name)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train function
def train_model():
    tracker = EmissionsTracker(output_dir=".", output_file="emissions.csv", measure_power_secs=1, log_level="error")
    tracker.start()

    with st.spinner("🚀 Training in progress..."):
        time.sleep(1)
        if model_type == "Random Forest":
            model = RandomForestClassifier(n_estimators=n_estimators)
        else:
            model = LogisticRegression(max_iter=max_iter)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

    emissions_kg = tracker.stop()
    emissions_g = emissions_kg * 1000
    return acc, emissions_g

# Function to convert emissions to real-world equivalents
def co2_to_real_world_equivalent(co2_emission_grams):
    equivalents = {
        "driving_car_120g_per_km": {"activity": "driving a petrol car", "equivalent": co2_emission_grams / 120},
        "boiling_kettle_10g_per_cup": {"activity": "boiling a kettle", "equivalent": co2_emission_grams / 10},
        "watching_youtube_4g_per_minute": {"activity": "watching YouTube (HD)", "equivalent": co2_emission_grams / 4},
        "human_breathing_1000g_per_day": {"activity": "breathing (human, per day)", "equivalent": co2_emission_grams / 1000}
    }
    
    equivalents_in_words = {}
    for key, value in equivalents.items():
        activity = value["activity"]
        equivalent_value = value["equivalent"]
        if equivalent_value < 1:
            equivalent_in_words = f"{equivalent_value * 1000:.2f} seconds"
        elif equivalent_value < 1000:
            equivalent_in_words = f"{equivalent_value:.2f} minutes"
        else:
            equivalent_in_words = f"{equivalent_value / 1000:.2f} hours"
        
        equivalents_in_words[activity] = equivalent_in_words
        
    return equivalents_in_words

# Train button
if st.button("🎯 Train Model & Track Emissions"):
    accuracy, emissions_g = train_model()
    st.success(f"✅ Accuracy: **{accuracy*100:.2f}%**, Emissions: **{emissions_g:.4f} g CO₂eq**")

    st.session_state.logs.append({
        "Dataset": dataset_name,
        "Model": model_type,
        "Params": f"{'Trees: ' + str(n_estimators) if model_type=='Random Forest' else 'Epochs: ' + str(max_iter)}",
        "Accuracy (%)": f"{accuracy*100:.4f}",
        "Emissions (g CO₂eq)": f"{emissions_g:.4f}"
    })

# Previous runs table
if st.session_state.logs:
    st.subheader("📋 Previous Runs")
    df_logs = pd.DataFrame(st.session_state.logs)
    st.dataframe(df_logs)

    # Emissions Chart
    st.subheader("📈 Emissions Chart")
    df_logs["Emissions (g CO₂eq)"] = df_logs["Emissions (g CO₂eq)"].astype(float)
    fig = px.line(df_logs, y="Emissions (g CO₂eq)", markers=True, title="Emissions per Training Run")
    st.plotly_chart(fig)

    # 🌿 Greenest configuration PER SELECTED DATASET
    st.subheader(f"🌍 Greenest Configuration (for {dataset_name} dataset)")
    filtered_df = df_logs[df_logs["Dataset"] == dataset_name]
    if not filtered_df.empty:
        min_emission_row = filtered_df.loc[filtered_df["Emissions (g CO₂eq)"].astype(float).idxmin()]
        st.markdown(f"""
        **Dataset:** {min_emission_row['Dataset']}  
        **Model:** {min_emission_row['Model']}  
        **Params:** {min_emission_row['Params']}  
        **Accuracy:** {min_emission_row['Accuracy (%)']}  
        **Emissions:** {min_emission_row['Emissions (g CO₂eq)']} g CO₂eq
        """)
    else:
        st.info("No training runs for this dataset yet.")

    # 🔁 Real-world CO₂ Equivalent for Latest Run
    st.subheader("📏 Real-world CO₂ Equivalent")
    latest_row = df_logs.iloc[-1]
    latest_grams = float(latest_row["Emissions (g CO₂eq)"])
    st.markdown(f"""
    **Dataset:** {latest_row['Dataset']}  
    **Model:** {latest_row['Model']}  
    **Params:** {latest_row['Params']}  
    **Accuracy:** {latest_row['Accuracy (%)']}  
    **Emissions:** {latest_grams:.4f} g CO₂eq  
  
- 📺 Watching YouTube (HD) for **{(latest_grams / 4) * 60:.4f} seconds**  
- 😮 Breathing (average human):  **{latest_grams / 1000 * 86400:.2f} seconds**
- 🚶‍♂️ Same CO₂ as walking **{latest_grams / 100:.6f} meters**  
- 🚗 Driving **{latest_grams / 120:.6f} meters** in a petrol car 
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
