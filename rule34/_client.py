from typing import Union, List

import httpx

from ._base_client import SyncAPIClient, AsyncAPIClient
from ._xml import XMLParser
from ._models import Post, Comment, Tag


class Rule34(SyncAPIClient):
    def __init__(self, *, timeout: Union[float, httpx.Timeout, None] = None) -> None:
        super().__init__(timeout=timeout)

    def search(
        self,
        tags: str,
        *,
        limit: Union[int, None] = None,
        page: Union[int, None] = None,
    ):
        add_params = {"tags": tags, "limit": limit, "pid": page}
        data = self.get(self.post_params, add_params).json()
        return list(map(lambda x: Post(**x), data))

    def get_post(self, post_id: int):
        add_params = {"id": post_id}
        data = self.get(self.post_params, add_params).json()
        return Post(**data[0])

    def get_comments(self, post_id: int):
        add_params = {"post_id": post_id}
        xml_content = self.get(self.comment_params, add_params).text
        return XMLParser.parse_comments(xml_content)

    def get_tags(self, *, tag_id: Union[int, None] = None):
        add_params = {"id": tag_id}
        xml_content = self.get(self.tag_params, add_params).text
        return XMLParser.parse_tags(xml_content)


class AsyncRule34(AsyncAPIClient):
    def __init__(self, *, timeout: Union[float, httpx.Timeout, None] = None) -> None:
        super().__init__(timeout=timeout)

    async def search(
        self,
        tags: str,
        *,
        limit: Union[int, None] = None,
        page: Union[int, None] = None,
    ):
        add_params = {"tags": tags, "limit": limit, "pid": page}
        data = (await self.get(self.post_params, add_params)).json()
        return list(map(lambda x: Post(**x), data))

    async def get_post(self, post_id: int):
        add_params = {"id": post_id}
        data = (await self.get(self.post_params, add_params)).json()
        return Post(**data[0])

    async def get_comments(self, post_id: int):
        add_params = {"post_id": post_id}
        xml_content = (await self.get(self.comment_params, add_params)).text
        return XMLParser.parse_comments(xml_content)

    async def get_tags(self, *, tag_id: Union[int, None] = None):
        add_params = {"id": tag_id}
        xml_content = (await self.get(self.tag_params, add_params)).text
        return XMLParser.parse_tags(xml_content)

