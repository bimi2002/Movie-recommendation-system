from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:bbb1234556@localhost/Movies")

def get_recommendations(genres, start, end):
    # If multiple genres are selected, filter using multiple LIKE conditions
    genre_conditions = " AND ".join(["m.genres LIKE %s"] * len(genres))  
    query = f"""
    SELECT m.title, m.genres, AVG(r.rating) AS avg_rating
    FROM movies m
    JOIN ratings r ON m.movie_id = r.movie_id
    WHERE ({genre_conditions}) 
      AND m.num_rates >= 50 
      AND m.release_year >= %s 
      AND m.release_year <= %s
    GROUP BY m.movie_id
    ORDER BY avg_rating DESC
    LIMIT 10;
    """
    
    # Convert genres into SQL wildcard format (e.g., "%Action%", "%Comedy%")
    genre_params = tuple(f"%{genre}%" for genre in genres)
    
    return pd.read_sql(query, engine, params=genre_params + (start, end))
