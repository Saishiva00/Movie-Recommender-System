import streamlit as st
import pickle
import pandas as pd
import gdown
import os

# Function to ensure similarity.pkl is available
def download_similarity():
    url = "https://drive.google.com/uc?id=1A-K3uSquBCTx9_3AjaJRiX-QCG5Evw1q"  # Google Drive file ID
    output = "similarity.pkl"
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)
    return output

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load movies dict
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Ensure similarity.pkl is present
similarity_file = download_similarity()
similarity = pickle.load(open(similarity_file, 'rb'))

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox("Choose a movie you like:", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")
    for i in recommendations:
        st.write(i)
