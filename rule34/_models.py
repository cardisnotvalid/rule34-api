from __future__ import annotations

from pydoc import locate
from dataclasses import dataclass, fields


__all__ = ["Post", "Comment", "Tag"]


@dataclass
class BaseModel:
    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], locate(field_type)):
                setattr(self, name, locate(field_type)(self.__dict__[name]))


@dataclass
class Post(BaseModel):
    preview_url: str
    sample_url: str
    file_url: str
    directory: int
    hash: str
    width: int
    height: int
    id: int
    image: str
    change: int
    owner: str
    parent_id: int
    rating: str
    sample: bool
    sample_height: int
    sample_width: int
    score: int
    tags: str
    source: str
    status: str
    has_notes: bool
    comment_count: int


@dataclass
class Comment(BaseModel):
    created_at: str
    post_id: int
    body: str
    creator: str
    id: int
    creator_id: int


@dataclass
class Tag(BaseModel):
    type: int
    count: int
    name: str
    ambiguous: bool
    id: int
