#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import pandas as pd
import streamlit as st


# In[4]:


# Load the trained model
model = pickle.load(open("solar_power_model.pkl", "rb"))

# Streamlit UI
st.title("Solar Power Prediction")

# Define valid input ranges
valid_ranges = {
    "distance_to_solar_noon": (0, 0.61),
    "temperature": (0, 150),
    "wind_direction": (0, 360),
    "wind_speed": (0, 100),
    "sky_cover": (0, 10),
    "visibility": (0, 100),
    "humidity": (0, 100),
    "average_wind_speed_period": (0, 100),
    "average_pressure_period": (0, 50),
}

# Collect user input
distance = st.number_input("Distance to Solar Noon (0 to 0.61)", min_value=0.0, max_value=0.61, step=0.01)
temperature = st.number_input("Temperature (0 to 150°F)", min_value=0.0, max_value=150.0, step=0.1)
wind_direction = st.number_input("Wind Direction (0 to 360°)", min_value=0.0, max_value=360.0, step=1.0)
wind_speed = st.number_input("Wind Speed (0 to 100 mph)", min_value=0.0, max_value=100.0, step=0.1)
sky_cover = st.number_input("Sky Cover (0 to 10)", min_value=0.0, max_value=10.0, step=1.0)
visibility = st.number_input("Visibility (0 to 100 miles)", min_value=0.0, max_value=100.0, step=0.1)
humidity = st.number_input("Humidity (0 to 100%)", min_value=0.0, max_value=100.0, step=0.1)
average_wind_speed = st.number_input("Average Wind Speed Period (0 to 100)", min_value=0.0, max_value=100.0, step=0.1)
average_pressure = st.number_input("Average Pressure Period (0 to 50)", min_value=0.0, max_value=50.0, step=0.1)

# Collect user inputs into a dictionary
user_inputs = {
    "distance_to_solar_noon": distance,
    "temperature": temperature,
    "wind_direction": wind_direction,
    "wind_speed": wind_speed,
    "sky_cover": sky_cover,
    "visibility": visibility,
    "humidity": humidity,
    "average_wind_speed_period": average_wind_speed,
    "average_pressure_period": average_pressure,
}

# Predict button
if st.button("Predict Power"):
    # Validate user input
    invalid_inputs = [
        (name, value) for name, value in user_inputs.items()
        if not (valid_ranges[name][0] <= value <= valid_ranges[name][1])
    ]

    if invalid_inputs:
        for name, value in invalid_inputs:
            st.error(f"❌ {name.replace('_', ' ').title()} must be between {valid_ranges[name][0]} and {valid_ranges[name][1]}. You entered: {value}")
    else:
        # Prepare data for prediction
        data = pd.DataFrame([list(user_inputs.values())], columns=user_inputs.keys())

        # Make prediction
        prediction = model.predict(data)[0]
        st.success(f"✅ Predicted Power Generation: {prediction:.2f} kW")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




