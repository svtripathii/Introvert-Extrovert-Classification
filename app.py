import streamlit as st
import numpy as np
import pickle

# -------------------------------
# Load Model and Scaler
# -------------------------------
with open("dt.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# with open("scaler.pkl", "rb") as scaler_file:
#     scaler = pickle.load(scaler_file)

# -------------------------------
# App Title
# -------------------------------
st.title("🧠 Personality Prediction: Introvert or Extrovert")
st.write("This app predicts whether a person is an **Introvert** or **Extrovert** based on behavioral traits.")

# -------------------------------
# User Inputs
# -------------------------------
st.header("📋 Enter Your Details")

time_alone = st.slider("1. Time Spent Alone (0–11 hrs)", 0, 11, 4)
social_events = st.slider("2. Social Event Attendance (0–10)", 0, 10, 3)
going_out = st.slider("3. Going Outside (0–7)", 0, 7, 3)
friends_circle = st.slider("4. Friends Circle Size (0–15)", 0, 15, 5)
post_freq = st.slider("5. Social Media Post Frequency (0–10)", 0, 10, 3)

stage_fear = st.radio("6. Do you have Stage Fear?", ["Yes", "No"])
drained = st.radio("7. Do you feel drained after socializing?", ["Yes", "No"])

# Convert categorical inputs
stage_fear_binary = 1 if stage_fear.lower() == "yes" else 0
drained_binary = 1 if drained.lower() == "yes" else 0

# -------------------------------
# Make Prediction
# -------------------------------
if st.button("Predict Personality"):
    # Prepare data
    user_data = np.array([[time_alone, social_events, going_out, friends_circle, post_freq]])
    # user_data_scaled = scaler.transform(user_data)

    # Combine scaled numerical + categorical
    final_input = np.concatenate((user_data, [[stage_fear_binary, drained_binary]]), axis=1)

    # Prediction
    prediction = model.predict(final_input)[0]
    #prob = model.predict_proba(final_input)[0][prediction]

    # Result
    #personality = "Extrovert" if prob > 0.5 else "Introvert"
    personality = "Extrovert" if prediction == 1 else "Introvert"
    st.success(f"### 🎯 Predicted Personality: **{personality}**")
    # st.info(f"Confidence: **{round(prob * 100, 2)}%**")

# Footer
st.markdown("---")
st.markdown("Built by **Saurav Tripathi** 🚀")
