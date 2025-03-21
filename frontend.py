import streamlit as st
import pandas as pd
from projekti import get_recommendations  # Import backend function
import base64

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/png;base64,{encoded_image}) no-repeat center center fixed;
            background-size: cover;
        }}
        .overlay {{
            background: rgba(0, 0, 0, 0.6); /* Dark overlay for readability */
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }}
        </style>
        <div class="overlay"></div>
        """,
        unsafe_allow_html=True
    )

# Set background image (change 'background.jpg' to your actual file path)
set_background("background3.png")  


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
