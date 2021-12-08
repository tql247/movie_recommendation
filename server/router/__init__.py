import os
import uvicorn
import psycopg2
from typing import List
from datetime import date

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from server.models.models import Location
import server.core.KNN as KNN
import server.core.SVD as SVD
import server.core.Search as Search


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://0.0.0.0:5500",
        "http://127.0.0.1:5500",
        "http://localhost:5000",
        "http://localhost:8000",
        "http://localhost:3000"
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def status():
    return {'mess': 'Good health!', 'status': 200}


@app.get("/history/{user_id}")
async def history(user_id: int):
    return {'mess': Search.search_history(user_id), 'status': 200}


@app.get("/recommendation/{user_id}")
async def recommendation(user_id: int):
    return {'mess': SVD.recommend_movies(user_id), 'status': 200}


@app.get("/search/{title}")
async def search(title: str):
    return {'mess': Search.search_by_title(title), 'status': 200}


@app.get("/relate/{movie_id}")
async def relate(movie_id: int):
    return {'mess': KNN.recommend(movie_id), 'status': 200}


# @app.get("/missing_data/v1")
# async def get(location: Location):
    # connection = psycopg2.connect(
    # user=os.environ['USER'],
    # password=os.environ['PASSWORD'],
    # host=os.environ['DB_SERVER'],
    # port=os.environ['DB_PORT'],
    # database=os.environ['DB_NAME'],
    # )

    # data = get_missing_data(connection, location.locations, location.date)
    # connection.close()
    # return data


# @app.get("/missing_data/v2")
# async def get(location: Location):
    # connection = psycopg2.connect(
    # user=os.environ['USER'],
    # password=os.environ['PASSWORD'],
    # host=os.environ['DB_SERVER'],
    # port=os.environ['DB_PORT'],
    # database=os.environ['DB_NEW'],
    # )

    # data = get_missing_data(connection, location.locations, location.date, True)
    # connection.close()
    # return data


# @app.get("/missing_data/v1/")
# async def get(date_request: date, locations: List[str] = Query(['BMT'], description="List of location name")):
    # connection = psycopg2.connect(
    # user=os.environ['USER'],
    # password=os.environ['PASSWORD'],
    # host=os.environ['DB_SERVER'],
    # port=os.environ['DB_PORT'],
    # database=os.environ['DB_NAME'],
    # )
    # data = get_missing_data(connection, locations, date_request)
    # connection.close()
    # return data


# @app.get("/missing_data/v2/")
# async def get(date_request: date, locations: List[str] = Query(['BMT'], description="List of location name")):
    # connection = psycopg2.connect(
    # user=os.environ['USER'],
    # password=os.environ['PASSWORD'],
    # host=os.environ['DB_SERVER'],
    # port=os.environ['DB_PORT'],
    # database=os.environ['DB_NEW'],
    # )
    # data = get_missing_data(connection, locations, date_request, True)
    # connection.close()
    # return data


# def test():
    # connection = psycopg2.connect(
    # user=os.environ['USER'],
    # password=os.environ['PASSWORD'],
    # host=os.environ['DB_SERVER'],
    # port=os.environ['DB_PORT'],
    # database=os.environ['DB_NAME'],
    # )
    # data = get_missing_data(connection, ["THANGLONG"], "2021-03-28")
    # connection.close()
    # return data


def run_app():
    uvicorn.run(app, host="0.0.0.0", port=8081)
