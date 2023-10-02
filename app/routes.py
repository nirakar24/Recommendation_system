from flask import render_template, request
from app import app
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import requests

# Load the dataset
df = pd.read_csv('data/movie.csv')
# print(df.columns)  # Print column names
# print(df.shape)


# Combine selected columns into a single string
df['combined_features'] = df['genres'] + ' ' + df['keywords'] + ' ' + df['overview']

# Define the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'].fillna(''))

# Calculate the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['movie_title']
        recommendations = recommend_movies(user_input)
        return render_template('index.html', recommendations=recommendations, user_input=user_input)

    return render_template('index.html', recommendations=None, user_input=None)

def recommend_movies(title, cosine_sim=cosine_sim):
    try:
        # Find the index of the movie with the given title
        movie_index = df.loc[df['title'] == title].index[0]

        # Calculate cosine similarity scores
        sim_scores = list(enumerate(cosine_sim[movie_index]))

        # Sort movies based on similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the top 10 similar movies (excluding the movie itself)
        sim_scores = sim_scores[1:2]

        # Get the movie index
        movie_indices = [i[0] for i in sim_scores]

        # Return the titles of recommended movies
        recommended_movies = []
        for index in movie_indices:
            # API
            name=df['title'].iloc[index]
            url = "https://online-movie-database.p.rapidapi.com/auto-complete"
            querystring = {"q":f"{name}"}
            headers = {
    	"X-RapidAPI-Key": "bbe73ef5aamsh0f75fe09e0f4d99p19bca7jsn7b79608943c5",
    	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            movie_name = name
            movie_entry = None
            for entry in data['d']:
                if entry.get('l') == movie_name:
                    movie_entry = entry
                    break
                
            if movie_entry:
                image_url = movie_entry['i']['imageUrl']
                print(image_url)
            else:
                print('Movie', movie_name, 'not found in the dictionary')
            movie_data = {
                'title': df['title'].iloc[index],
                #API
                'Image_URL': image_url  # Placeholder image URL
            }
            recommended_movies.append(movie_data)

        return recommended_movies
    except IndexError:
        return ["Movie not found in the dataset"]




