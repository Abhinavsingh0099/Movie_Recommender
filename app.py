import pickle
import pandas as pd
import streamlit as st


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Load data and models
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',  # Label for the widget
    movies['title']  # List of options (assuming 'movies' DataFrame contains a 'title' column)
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    for i in recommendations:
        st.write(i)

    # if recommendations:
    #     st.write("Recommended Movies:")
    #     for i, recommendation in enumerate(recommendations, start=1):
    #         st.write(f"{i}. {recommendation}")
    # else:
    #     st.write("No recommendations found.")



