import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds


ratings_df = pd.read_csv('ml-1m/ratings.dat', sep='::', names=['UserID', 'MovieID', 'Rating', 'Timestamp'], encoding='latin-1', engine='python')
movies_df = pd.read_csv('ml-1m/movies.dat', sep='::', names=['MovieID', 'Title', 'Genres'], encoding='latin-1', engine='python')
R_df = ratings_df.pivot(index = 'UserID', columns ='MovieID', values = 'Rating')
users_mean=np.array(R_df.mean(axis=1))

R_unsparsed=R_df.fillna(0).values

U, sigma, Vt = svds(R_unsparsed, k = 50)

sigma = np.diag(sigma)

all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt)

preds_df = pd.DataFrame(all_user_predicted_ratings, columns = R_df.columns)


def recommend_movies(userID, ratings_df=ratings_df, preds_df=preds_df, num_recommendations=10):
    # get rated movies id
    rated_movies_id = ratings_df[ratings_df.UserID == userID].MovieID.values

    # get predict for users
    pred_user_by_id = preds_df.iloc[userID - 1].reset_index()
    
    # get item not rated
    not_rated_item = pred_user_by_id[~pred_user_by_id.MovieID.isin(rated_movies_id)]
    
    note_rated_item_sorted = not_rated_item.sort_values(userID - 1, ascending=False)
    
    movie_recommend_id = note_rated_item_sorted.MovieID.values[:num_recommendations]

    return movies_df.set_index("MovieID").loc[movie_recommend_id].values.tolist()


def predict(user_id, movie_id, ratings_df=ratings_df, preds_df=preds_df, num_recommendations=10):
    pred_user_by_id = preds_df.iloc[user_id - 1].reset_index()

    # get predict for users by movies
    predict_value = pred_user_by_id[pred_user_by_id.MovieID == movie_id].values[0][1] + users_mean[user_id - 1]

    # return value from 1-5
    return min(max(predict_value, 1), 5)

# print(recommend_movies(ratings_df, preds_df, 14))