# Introvert vs Extrovert Personality Classification

This project uses supervised machine learning to classify people as **Introverts** or **Extroverts** based on their behaviors and social traits. It includes data processing, model training, evaluation, and a Streamlit-based web app for making predictions.
---

## Problem Statement

Classifying personality can help with personalization, mental health, education, and team dynamics. This project aims to predict if someone is an introvert or extrovert by looking at factors like time spent alone, social habits, and posting frequency.
---

## Dataset Features

| Feature                   | Description                          |
|---------------------------|--------------------------------------|
| `Time_spent_Alone`        | Hours per day spent alone (0–11)     |
| `Stage_fear`              | Binary: Yes/No                       |
| `Social_event_attendance`| Events attended per month (0–10)     |
| `Going_outside`           | Days per week going outside (0–7)    |
| `Drained_after_socializing` | Binary: Yes/No                    |
| `Friends_circle_size`     | Number of close friends (0–15)       |
| `Post_frequency`          | Social media posts per week (0–10)   |
| **`Personality`**         | Target: Introvert or Extrovert       |
---

## Objective

Create a machine learning model to classify a person’s personality trait and deploy it using a Streamlit web interface.
---

## Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Matplotlib**, **Seaborn**
- **Streamlit**
- **Pickle** (for model saving)

- ## Model

- **Logistic Regression** (used as the baseline model)
- Trained with scaled features using **MinMaxScaler**
- Evaluated using accuracy and a confusion matrix
---

## Highlights

- Cleaned and processed both categorical and numerical data
- Scaled user input for improved predictions
- Saved the model and scaler for future use
- Created an interactive UI using Streamlit
---

## How to Run the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/introvert-extrovert-classification.git
   cd introvert-extrovert-classification

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
---

## Use Cases  

1. Personalized recommendation systems  

2. Mental health and self-awareness platforms  

3. Education platforms for learning style adjustment  

4. Social networking behavior analysis  

5. HR and recruitment personality insights
---

## Folder Structure 

├── app.py                  # Streamlit app
├── model.pkl               # Pickled ML model
├── scaler.pkl              # Pickled scaler
├── data.csv                # Dataset (optional)
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
---

## Contact
For any queries or collaborations, email me at sauravtripathi72@gmail.com.
