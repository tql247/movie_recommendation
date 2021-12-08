import pandas as pd
import numpy as np
import server.core.SVD as SVD

movies_df = pd.read_csv('ml-1m/movies.dat', sep='::', names=['MovieID', 'Title', 'Genres'], encoding='latin-1', engine='python')
ratings_df = pd.read_csv('ml-1m/ratings.dat', sep='::', engine='python', names=['user_id', 'movie_id', 'rating', 'unix_timestamp'], encoding='latin-1')


def search_by_title(title, user_id=None):
    top_10_title = movies_df[movies_df["Title"].str.contains(title)][:5]
    ratings = list()

    return top_10_title.values.tolist(), ratings

def search_history(user_id):
    movie_id_rated = ratings_df[ratings_df['user_id'] == user_id]['movie_id'].values.tolist()
    movies_rated = movies_df[movies_df['MovieID'].isin(movie_id_rated)].values.tolist()

    return movies_rated