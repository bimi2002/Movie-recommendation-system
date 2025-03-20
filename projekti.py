from sqlalchemy import create_engine
import pandas as pd

# Create the engine
engine = create_engine("postgresql://postgres:bbb1234556@localhost/Movies")

def get_recommendations(genre_filter, start, end):
    query = f"""
    SELECT m.title, m.genres, AVG(r.rating) AS avg_rating
    FROM movies m
    JOIN ratings r ON m.movie_id = r.movie_id
    WHERE ({' OR '.join(["m.genres LIKE %s"] * len(genre_filter))}) 
      AND m.num_rates >= 50 
      AND m.release_year >= %s 
      AND m.release_year <= %s
    GROUP BY m.movie_id
    ORDER BY avg_rating DESC
    LIMIT 10;
    """
    return pd.read_sql(query, engine, params=tuple(f"%{g}%" for g in genre_filter) + (start, end))


# Example usage
genre = "Drama"
df = get_recommendations(genre,1000,1990)
print(df)