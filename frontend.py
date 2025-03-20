import streamlit as st
import pandas as pd
from projekti import get_recommendations  # Import backend function

# 🎬 Streamlit UI
st.title("🎥 Movie Recommendation System")

# Genre Selection
genre = st.text_input("Enter Genre (e.g., Action, Comedy, Drama):", "Action")

# Year Range
start_year, end_year = st.slider("Select Year Range:", 1900, 2025, (2000, 2015))

# Fetch & Display Recommendations
if st.button("Get Recommendations"):
    recommendations = get_recommendations(genre, start_year, end_year)
    if recommendations.empty:
        st.warning("No movies found. Try another genre or adjust the year range.")
    else:
        st.write("### 📌 Top Movies:")
        st.dataframe(recommendations)
