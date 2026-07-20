from fastapi import APIRouter,Path,status
from fastapi.responses import JSONResponse
from database import db_dependency
from typing import Literal

from schemas import MovieCreate,MovieUpdate
from curd import get_all_movies,get_single_movie,create_new_movie,update_movie,delete_movie,get_sorted_movies

router = APIRouter(tags=["Movies"])

@router.get("/movies")
def get_All_Movies(db:db_dependency):
    return get_all_movies(db)

@router.get("/movies/sort")
def sort_Movies(db:db_dependency,sort_by:Literal["duration","rating"] = "rating", order : Literal["asc","desc"] = "desc"):
    movies = get_sorted_movies(db,sort_by,order)
    return movies



@router.get("/movies/{movie_id}",status_code=status.HTTP_200_OK)
def get_Single_Movie(db:db_dependency,movie_id:int = Path(...,description="ID of the movie",examples=['1','2','3'])):

    movie = get_single_movie(db,movie_id)

    return {'movie':movie}

@router.post("/create_movies",status_code=status.HTTP_201_CREATED)
def create_New_Movie(db:db_dependency,new_movie:MovieCreate):
    movie = create_new_movie(db,new_movie)

    return {"message":"New movie created successfully","new movie":movie}

@router.put("/movies/{movie_id}",status_code=status.HTTP_200_OK)
def upDate_Movie(db:db_dependency, upMovie:MovieUpdate ,movie_id:int = Path(...,description="ID of the movie",examples=['1','2','3'])):
    movie = update_movie(db,movie_id,upMovie)
    return{"message":"Movie update successfully","update movie":movie}


@router.delete("/movies/{movie_id}",status_code=status.HTTP_200_OK)
def delete_Movie(db:db_dependency,movie_id:int = Path(...,description="ID of the movie",examples=['1','2','3'])):
    delete_movie(db,movie_id)
    return {"message":"Movie delete successfully"}

