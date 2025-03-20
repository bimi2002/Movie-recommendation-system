import streamlit as st
import pandas as pd
from projekti import get_recommendations  # Import backend function

# 🎬 Streamlit UI
st.title("🎥 Movie Recommendation System")

# List of genres
genres = [
    'Adventure', 'Children', 'Fantasy', 'Animation', 'Action', 
    'Horror', 'Musical', 'Sci-Fi', 'Romance', 'Thriller', 'Documentary', 'Drama', 
    'War', 'Comedy', 'Crime', 'IMAX', 'Mystery', 'Western', 'Film-Noir'
]

# Genre selection using buttons
st.subheader("Select a Genre:")
selected_genre = st.radio("Genres", genres, horizontal=True, index=5)  # Default to 'Action'

# Year range selection
start_year, end_year = st.slider("Select Year Range:", 1900, 2025, (2000, 2015))

# Fetch & Display Recommendations
if st.button("Get Recommendations"):
    recommendations = get_recommendations(selected_genre, start_year, end_year)
    if recommendations.empty:
        st.warning("No movies found. Try another genre or adjust the year range.")
    else:
        st.write(f"### 📌 Top {selected_genre} Movies:")
        st.dataframe(recommendations)
