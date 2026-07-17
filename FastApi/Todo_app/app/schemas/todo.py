from pydantic import BaseModel, ConfigDict,Field
from typing import Optional

class CreateTodo(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    completed: bool

class UpdateTodo(BaseModel):
    title: Optional[int] = Field(default=None)
    description: Optional[int] = Field(default=None)
    priority: Optional[int] = Field(default=None)
    completed: Optional[bool] = Field(default=None)