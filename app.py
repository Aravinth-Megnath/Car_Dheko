import streamlit as st
import pandas as pd
import joblib

from steering_type import CleaningSteeringType
from tyre import CleanTyreType

st.title("Car Price Prediction")

model = joblib.load('car_pipeline.pkl')

df = pd.read_csv('future_df.csv')



predict = model.predict(df)

df['Predicted Price'] = predict

st.write(df)