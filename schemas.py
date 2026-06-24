from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class UserBase(BaseModel):
    pass
class PostCreate(UserBase):
    pass
class PostResponse(UserBase):
    pass

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str

