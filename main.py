import streamlit as st  # For creating web interface
import pandas as pd  # For data manipulation
import datetime  # For handling dates
import csv  # For reading and writing CSV files
import os  # For file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    try:
        data = pd.read_csv(MOOD_FILE, encoding="utf-8")
        if "Date" not in data.columns or "Mood" not in data.columns:
            return pd.DataFrame(columns=["Date", "Mood"])
        return data
    except Exception as e:
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])
        writer.writerow([date, mood])

# Streamlit app title
st.title("😊 Mood Tracker 📊")

# Get today's date
today = datetime.date.today()

# Mood input section
st.subheader("How are you feeling today? 🤔")
mood = st.selectbox("Select your mood", ["😀 Happy", "😢 Sad", "😡 Angry", "😐 Neutral"])

# Button to save mood
if st.button("Log Mood 📝"):
    save_mood_data(today, mood)
    st.success("✅ Mood Logged Successfully!")

# Load and display existing mood data
data = load_mood_data()
if not data.empty:
    st.subheader("📈 Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data = data.dropna(subset=["Date"])
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)

# Footer credit
st.write("Built with ❤️ by [Zuhii Shah ](https://github.com/ZuhiiMalakShah) ")
