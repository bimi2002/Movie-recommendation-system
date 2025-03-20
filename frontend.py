import streamlit as st
import pandas as pd
from projekti import get_recommendations  # Import backend function

st.title("🎥 Movie Recommendation System")

genres = [
    'Adventure', 'Children', 'Fantasy', 'Animation', 'Action', 
    'Horror', 'Musical', 'Sci-Fi', 'Romance', 'Thriller', 'Documentary', 'Drama', 
    'War', 'Comedy', 'Crime', 'IMAX', 'Mystery', 'Western', 'Film-Noir'
]

# Multi-genre selection
st.subheader("Select Genres:")
selected_genres = st.multiselect("Genres", genres, default=["Action"])

# Year range selection
start_year, end_year = st.slider("Select Year Range:", 1900, 2025, (2000, 2015))

if st.button("Get Recommendations"):
    if selected_genres:
        recommendations = get_recommendations(selected_genres, start_year, end_year)
        if recommendations.empty:
            st.warning("No movies found. Try different genres or adjust the year range.")
        else:
            st.write(f"### 📌 Top Movies for {', '.join(selected_genres)}:")
            st.dataframe(recommendations)
    else:
        st.warning("Please select at least one genre.")
