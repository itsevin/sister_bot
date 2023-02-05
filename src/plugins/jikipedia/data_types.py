from typing import Optional

from pydantic import BaseModel


class DefinitionImages(BaseModel):
    class Full(BaseModel):
        path: str
        # more...

    full: Full
    # more...


class DefinitionTerm(BaseModel):
    title: str
    # more...


class DefinitionTag(BaseModel):
    name: str
    # more...


class Definition(BaseModel):
    id: int
    images: list[DefinitionImages]
    term: DefinitionTerm
    content: str
    plaintext: str
    tags: list[DefinitionTag]
    # more...


class JikiResponseData(BaseModel):
    definitions: list[Definition]
    # more...


class ErrMessage(BaseModel):
    title: str
    content: str


class JikiResponse(BaseModel):
    data: Optional[list[JikiResponseData]]

    # err
    message: Optional[str | ErrMessage]
    category: Optional[str]
    information: Optional[str]
