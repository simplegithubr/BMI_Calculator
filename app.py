import streamlit as st

import pandas as pd
st.set_page_config(page_title="Kinzaa's BMI Calculator", layout="centered")

st.title("💖Welcome to By Creative Kinza Bami Calculator 🎨")

heght= st.slider("📏Enter Your Heght(in cm):" , 100, 125, 250)
weight = st.slider("⚖️Enter Your weight(in kg):" , 40, 200, 70)
bmi = weight / ((heght/100) **2)
st.write(f"💡Your BMI is {bmi:.2f}")
st.write("### 🏆BMI Categories 🏆 ### ")
st.write("🟢 Underweight: BMI less then 18.5")
st.write("🟡 Normal weighit: BMI between 18.5 and 24.9")
st.write("🟠 Overwighit: BMI between 25 and 29.9")
st.write("🔴 Obesity: BMI 30 or greater")

if bmi < 18.5:
    st.write("⚠️ *You're underweight! Eat healthy and stay strong!* 💪")
elif 18.5 <= bmi <= 24.9:
    st.write("✅ *Great! You have a normal weight. Keep it up!* 🎉")
elif 25 <= bmi <= 29.9:
    st.write("⚠️ *You're overweight! Try to maintain a balanced diet and exercise.* 🏃")
else:
    st.write("🚨 *You're in the obesity range! Consider a healthy lifestyle change.* 🍏")