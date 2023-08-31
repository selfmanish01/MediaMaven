import streamlit as st
import pickle
import requests

# Set the title of the Streamlit app
st.title("MediaMaven")

# Load the preprocessed movie data and similarity matrix
movie_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_list1 = movie_list
movie_list = movie_list['title'].values

# Create a dropdown for selecting a movie
selected_movie_name = st.selectbox('Choose movie', movie_list)

# Function to fetch the poster image URL for a given movie ID
def fetchposter(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={your api key}'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function to fetch the homepage URL for a given movie ID
def fetchhomepage(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={your api key}'.format(movie_id))
    data = response.json()
    return data["homepage"]

# Function to recommend similar movies
def recommend(movie):
    movie_index = movie_list1[movie_list1['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    homepage = []
    movie_idapp = []
    for i in movies_list:
        movie_id = movie_list1.iloc[i[0]].movie_id
        recommended_movies.append(movie_list1.iloc[i[0]].title)
        recommended_movies_poster.append(fetchposter(movie_id))
        homepage.append(fetchhomepage(movie_id))
        movie_idapp.append(movie_id)
        print(movie_idapp)
    return recommended_movies, recommended_movies_poster, movie_idapp

# When the 'Recommend' button is clicked
if st.button('Recommend'):
    # Call the recommend function and get the recommended movie details
    recommended_names, recommended_posters, recommended_movie_ids = recommend(selected_movie_name)

    # Display the recommended movies and their posters
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_names[0])
        st.image(recommended_posters[0])
        url = "https://hitendra007.github.io/movie_app/details.html?id={}".format(recommended_movie_ids[0])
        st.write("Check out this [link](%s)" % url)
    with col2:
        st.text(recommended_names[1])
        st.image(recommended_posters[1])
        url = "https://hitendra007.github.io/movie_app/details.html?id={}".format(recommended_movie_ids[1])
        st.write("Check out this [link](%s)" % url)
    with col3:
        st.text(recommended_names[2])
        st.image(recommended_posters[2])
        url = "https://hitendra007.github.io/movie_app/details.html?id={}".format(recommended_movie_ids[2])
        st.write("Check out this [link](%s)" % url)
    with col4:
        st.text(recommended_names[3])
        st.image(recommended_posters[3])
        url = "https://hitendra007.github.io/movie_app/details.html?id={}".format(recommended_movie_ids[3])
        st.write("Check out this [link](%s)" % url)
    with col5:
        st.text(recommended_names[4])
        st.image(recommended_posters[4])
        url = "https://hitendra007.github.io/movie_app/details.html?id={}".format(recommended_movie_ids[4])
        st.write("Check out this [link](%s)" % url)