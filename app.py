import streamlit as st
import pickle
import os
import gdown
import pandas as pd

# Use absolute paths so it works regardless of working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_data():
    # Fix for movies_dict.pkl — absolute path
    movies_dict_path = os.path.join(BASE_DIR, 'movies_dict.pkl')
    movies_dict = pickle.load(open(movies_dict_path, 'rb'))
    movies = pd.DataFrame(movies_dict)

    # Fix for similarity.pkl — gdown v6 uses id= parameter, no fuzzy
    similarity_path = os.path.join(BASE_DIR, 'similarity.pkl')
    if not os.path.exists(similarity_path):
        file_id = "1Uz2RvPeuGyr3KwdlRntQ7XvS7N2BvjRF"
        gdown.download(id=file_id, output=similarity_path, quiet=False)
    similarity = pickle.load(open(similarity_path, 'rb'))

    return movies, similarity

movies, similarity = load_data()

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('🎬 Movie Recommender System')
selected_movie = st.selectbox('Select a movie', movies['title'].values)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write(movie)
