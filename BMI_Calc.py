# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 21:17:50 2026

@author: Ansari
"""

import streamlit as st

# 1. Set up the title and description
st.title("Simple BMI Calculator")
st.write("Enter your details below to calculate your Body Mass Index.")

# 2. Create input fields for weight and height
# We use columns to make the UI look cleaner
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (in kg)", min_value=1.0, value=70.0)

with col2:
    # We take height in centimeters as it's more common, then convert to meters
    height_cm = st.number_input("Height (in cm)", min_value=1.0, value=170.0)
    height_m = height_cm / 100

# 3. Calculate BMI when the user clicks the button
if st.button("Calculate BMI"):
    if height_m > 0:
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)
        
        st.subheader(f"Your BMI is: {bmi}")
        
        # 4. Determine the category
        if bmi < 18.5:
            st.warning("Category: Underweight")
        elif 18.5 <= bmi <= 24.9:
            st.success("Category: Normal weight")
        elif 25 <= bmi <= 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obesity")
    else:
        st.error("Height must be greater than zero.")