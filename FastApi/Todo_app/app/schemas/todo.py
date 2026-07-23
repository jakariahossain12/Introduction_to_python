from pydantic import BaseModel, ConfigDict,Field
from typing import Optional

class CreateTodo(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    completed: bool

class UpdateTodo(BaseModel):
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    priority: Optional[int] = Field(default=None)
    completed: Optional[bool] = Field(default=None)