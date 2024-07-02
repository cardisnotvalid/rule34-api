from __future__ import annotations

from typing import NamedTuple, List, Dict, Any


__all__ = ["Post", "Comment", "Tag"]


class Post(NamedTuple):
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

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Post":
        return Post(
            preview_url=data["preview_url"],
            sample_url=data["sample_url"],
            file_url=data["file_url"],
            directory=data["directory"],
            hash=data["hash"],
            width=data["width"],
            height=data["height"],
            id=data["id"],
            image=data["image"],
            change=data["change"],
            owner=data["owner"],
            parent_id=data["parent_id"],
            rating=data["rating"],
            sample=data["sample"],
            sample_height=data["sample_height"],
            sample_width=data["sample_width"],
            score=data["score"],
            tags=data["tags"],
            source=data["source"],
            status=data["status"],
            has_notes=data["has_notes"],
            comment_count=data["comment_count"],
        )


class Comment(NamedTuple):
    created_at: str
    post_id: int
    body: str
    creator: str
    id: int
    creator_id: int

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Comment":
        return Comment(
            created_at=data["created_at"],
            post_id=int(data["post_id"]),
            body=data["body"],
            creator=data["creator"],
            id=int(data["id"]),
            creator_id=int(data["creator_id"]),
        )


class Tag(NamedTuple):
    type: int
    count: int
    name: str
    ambiguous: bool
    id: int

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Tag":
        return Tag(
            type=int(data["type"]),
            count=int(data["count"]),
            name=data["name"],
            ambiguous=data["ambiguous"],
            id=int(data["id"]),
        )
