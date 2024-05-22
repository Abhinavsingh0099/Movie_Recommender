import pickle
import pandas as pd
import streamlit as st

# Function to recommend movies based on similarity
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
        return recommended_movies
    except IndexError:
        return ["Movie not found in the dataset"]

# Load data and models
try:
    with open('movie_dict.pkl', 'rb') as f:
        movies_dict = pickle.load(f)
    movies = pd.DataFrame(movies_dict)
    
    with open('similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    st.error("Error: Pickle files not found. Make sure you have the correct file paths.")
    st.stop()
except pickle.UnpicklingError:
    st.error("Error: Unable to unpickle files. The files might be corrupted.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the pickle files: {e}")
    st.stop()

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',  # Label for the widget
    movies['title']  # List of options (assuming 'movies' DataFrame contains a 'title' column)
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
