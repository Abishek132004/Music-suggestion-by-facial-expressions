import streamlit as st
import subprocess

st.set_page_config(page_title="Music Recommendation", layout="wide")

# Custom CSS for better UI
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #FF5733;
        }
        .stButton>button {
            width: 100%;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            color: white;
            border-radius: 10px;
        }
        .emotion-button { background-color: #3498db; }
        .train-button { background-color: #2ecc71; }
        .recommend-button { background-color: #e74c3c; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Music Recommendation by Facial Emotions using CNN</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Add Emotion", key="add", help="Start collecting facial emotion data"):
        subprocess.run(["python", "data_collection.py"])

with col2:
    if st.button("Save Emotions", key="save", help="Train the model with collected emotions"):
        subprocess.run(["python", "data_training.py"])

with col3:
    if st.button("Recommend Songs", key="recommend", help="Get song recommendations based on your emotions"):
        subprocess.Popen(["streamlit","run", "music.py"])
