from pydantic import BaseModel,Field
from typing import Optional,Annotated,Literal

class MovieCreate(BaseModel):
    movie_id : Annotated[int,Field(...,description='ID of the movie')]
    title : Annotated[str,Field(...,description='Title of the movie')]
    director : Annotated[str,Field(...,description='Director name of the movie')]
    genre: Annotated[Literal["action","comedy","drama","thriller"],Field(...,description='Genre of the movie')]
    duration : Annotated[int,Field(...,gt=0,description='Total runtime of the movie in minutes')]
    rating : Annotated[float,Field(...,ge=0.0,le=5.0,description='Movie rating')]


class MovieUpdate(BaseModel):
    movie_id : Annotated[Optional[int],Field(None,description='ID of the movie')]
    title : Annotated[Optional[str],Field(None,description='Title of the movie')]
    director : Annotated[Optional[str],Field(None,description='Director name of the movie')]
    genre: Annotated[Optional[Literal["action","comedy","drama","thriller"]],Field(None,description='Genre of the movie')]
    duration : Annotated[Optional[int],Field(None,description='Total runtime of the movie in minutes')]
    rating : Annotated[Optional[float],Field(None,description='Movie rating')]
