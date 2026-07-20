from sqlalchemy.orm import Session
from sqlalchemy import desc,asc
from models import Movies
from fastapi import HTTPException
from schemas import MovieCreate,MovieUpdate

def get_all_movies(db:Session):
    return db.query(Movies).all()


def get_single_movie(db:Session,movie_id:int):
    movie = db.query(Movies).filter(Movies.movie_id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=404,detail="Movie not found")
    
    return movie


def create_new_movie(db:Session,new_movie:MovieCreate):
    exists_movie = db.query(Movies).filter(Movies.movie_id == new_movie.movie_id).first()

    if exists_movie:
        raise HTTPException(status_code=400,detail="this movie already exists")
    
    movie = Movies(**new_movie.model_dump())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def update_movie(db:Session,movie_id:int,movie:MovieUpdate):
    exists_movie = db.query(Movies).filter(Movies.movie_id == movie_id).first()

    if not exists_movie:
        raise HTTPException(status_code=404,detail="Movie not found")
    
    updateMovie = movie.model_dump(exclude_unset=True)

    for key,value in updateMovie.items():
        setattr(exists_movie,key,value)
    
    db.commit()
    db.refresh(exists_movie)
    return exists_movie


def delete_movie(db:Session,movie_id:int):
    movie = db.query(Movies).filter(Movies.movie_id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=404,detail="Movie not found")
    
    db.query(Movies).filter(Movies.movie_id == movie_id).delete()
    db.commit()

def get_sorted_movies(db:Session,sort_by:str,order:str):
    query = db.query(Movies)

    if sort_by == "duration":
        sort = Movies.duration
    else:
        sort = Movies.rating
    
    if order == "asc":
        query = query.order_by(asc(sort))
    else: 
        query = query.order_by(desc(sort))
    
    return query.all()