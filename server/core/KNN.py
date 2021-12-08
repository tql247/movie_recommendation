#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action='ignore')
import re
from sklearn.feature_extraction.text import CountVectorizer


movies = pd.read_csv('ml-1m/movies.dat', sep='::', engine='python', names=['movie_id', 'title', 'genres'], encoding='latin-1')
ratings = pd.read_csv('ml-1m/ratings.dat', sep='::', engine='python', names=['user_id', 'movie_id', 'rating', 'unix_timestamp'], encoding='latin-1')
users = pd.read_csv('ml-1m/users.dat', sep='::', engine='python', names=["user_id", "Gender", "Age", "Occupation", "Zip-code"], encoding='latin-1')


moviesandratings = pd.merge(left=movies,right=ratings,how='inner',on='movie_id')
movieratingsusers = pd.merge(left=moviesandratings,right=users,how='inner',on='user_id')


data = movieratingsusers.copy()
data.drop(['unix_timestamp','Zip-code'],axis=1,inplace=True)



def search_name(movie_name):
      return(re.search("Toy Story".lower(),movie_name.lower()) is not None)

data['Toy_Story']=data['title'].apply(search_name)

Toy_Story  = data[data.Toy_Story==True]


Toy_Story.groupby(['title','rating']).count()['user_id']


df = ratings.pivot(index = 'movie_id', columns = 'user_id', values = 'rating')


df.fillna(0,inplace=True)



no_user_voted = ratings.groupby('movie_id')['rating'].agg('count')


no_movies_voted = ratings.groupby('user_id')['rating'].agg('count')


df = df.loc[no_user_voted[no_user_voted > 10].index, :]


#setting user_rating threshold
df = df.loc[:, no_movies_voted[no_movies_voted > 50].index]

#remove sparsity
from scipy.sparse import csr_matrix
crs_data = csr_matrix(df.values)
df.reset_index(inplace = True)

#creating model using knn
from sklearn.neighbors import NearestNeighbors
knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute', n_neighbors = 20, n_jobs = -1)
knn.fit(crs_data)


#creating function for recommendation
def recommend(movie_id):
    movies_to_recommend = 10
    distances, indices = knn.kneighbors(crs_data[movie_id], n_neighbors = movies_to_recommend +1)
    movie_indices = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key = lambda x :x[1])[:0:-1]
    
        
    recommend_frame = []
    for i in movie_indices:
        movie_id = df.iloc[i[0]]['movie_id']
        id_ = movies[movies['movie_id'] == movie_id].index
        
        recommend_frame.append({'title': movies.iloc[id_]['title'].values[0], 'genres': movies.iloc[id_]['genres'].values[0], 'Distance': i[1]})
        
    output = pd.DataFrame(recommend_frame, index=range(1, movies_to_recommend+1))
    return output.values.tolist()
