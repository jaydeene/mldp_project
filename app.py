import streamlit as st
import joblib
import pandas as pd


model = joblib.load('best_random_forest_model.pkl')


st.title("Car Selling Price Prediction")

car_model = st.text_input("Enter Car Model")
year = st.number_input("Enter Car Year", min_value=2000, max_value=2025, value=2020)
km_driven = st.number_input("Enter Kilometers Driven", min_value=0, value=50000)
mileage = st.number_input("Enter Mileage (km/l)", min_value=0.0, value=15.0)
engine = st.number_input("Enter Engine Capacity (cc)", min_value=0, value=1500)
max_power = st.number_input("Enter Max Power (bhp)", min_value=0.0, value=100.0)
seats = st.number_input("Enter Number of Seats", min_value=2, max_value=8, value=5)

fuel = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
transmission = st.selectbox("Select Transmission", ["Manual", "Automatic"])
seller_type = st.selectbox("Select Seller Type", ["Individual", "Trustmark Dealer"])
owner = st.selectbox("Select Number of Owners", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"])


fuel_mapping = {"Petrol": 1, "Diesel": 2, "CNG": 3, "LPG": 4}
transmission_mapping = {"Manual": 0, "Automatic": 1}
seller_type_mapping = {"Individual": 0, "Trustmark Dealer": 1}
owner_mapping = {"First Owner": 1, "Second Owner": 2, "Third Owner": 3, "Fourth & Above Owner": 4}

fuel_value = fuel_mapping[fuel]
transmission_value = transmission_mapping[transmission]
seller_type_value = seller_type_mapping[seller_type]
owner_value = owner_mapping[owner]

input_data = {
    'car_model': car_model,
    'year': year,
    'km_driven': km_driven,
    'mileage': mileage,
    'engine': engine,
    'max_power': max_power,
    'seats': seats,
    'fuel': fuel_value,
    'transmission': transmission_value,
    'seller_type': seller_type_value,
    'owner': owner_value
}

df_input = pd.DataFrame([input_data])

if st.button("Predict Car Price"):
    prediction = model.predict(df_input)
    st.success(f"Predicted Selling Price: ₹{prediction[0]:,.2f}")
