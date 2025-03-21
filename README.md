# 🎬 Movie Recommendation System  

A simple **movie recommendation system** using **PostgreSQL, Python, and Streamlit** to provide **personalized movie suggestions** based on user ratings.  

## 🚀 Features  
- **Top-rated movies** by genre  
- **User-specific recommendations**  
- **Filter by rating count** (Only movies with at least 50 ratings)  
- **Streamlit UI** for an interactive experience  

## 🛠️ Tech Stack  
- **PostgreSQL** (Database)  
- **SQLAlchemy** (Database connection)  
- **Pandas** (Data processing)  
- **Streamlit** (Web UI)  

# 📖 Data Base Construction
## movie table contains:
- movie_id
- rating
- title
- genres
- num_rates 
- release_year
## ratings table contains:
- rating_id
- user_id
- movie_id
- rating
- date 

## The Link to the dataset
[movies data](https://grouplens.org/datasets/movielens/latest/)