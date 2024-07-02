from typing import TypeVar, Generic, Union, Dict, List, Any
import random

import httpx
from httpx import URL, Timeout, Request, Response

from ._xml import XMLParser
from ._models import Post, Comment, Tag


_HttpxClientT = TypeVar("HttpxClientT", bound=[httpx.Client, httpx.AsyncClient])


class BaseClient(Generic[_HttpxClientT]):
    _client: _HttpxClientT
    _base_url: URL
    _timeout: Timeout

    def __init__(
        self,
        *,
        base_url: str = "https://api.rule34.xxx",
        timeout: float = 30.0
    ) -> None:
        self._base_url = URL(base_url)
        self._timeout = Timeout(timeout)

    def _format_tags(self, tags: str) -> str:
        return "%20".join("_".join(tag.split()) for tag in tags.split(","))

    def _build_params(
        self,
        base_params: Dict[str, Any],
        add_params: Dict[str, Any]
    ) -> Dict[str, Any]:
        return self._prepare_params({**base_params, **add_params})

    def _prepare_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        xparams = {}
        for key, value in params.items():
            if value is not None:
                if key == "tags":
                    value = self._format_tags(value)
                xparams[key] = value
        return xparams

    def _build_request(self, method: str, params: Dict[str, Any]) -> Request:
        return self._client.build_request(
            method=method,
            url=self._base_url.copy_with(path="/index.php"),
            params=self._prepare_params(params),
            timeout=self._timeout
        )

    @property
    def default_params(self) -> Dict[str, Any]:
        return {"page": "dapi", "q": "index"}

    @property
    def post_params(self) -> Dict[str, Any]:
        return {**self.default_params, "s": "post", "json": 1}

    @property
    def comment_params(self) -> Dict[str, Any]:
        return {**self.default_params, "s": "comment"}

    @property
    def tag_params(self) -> Dict[str, Any]:
        return {**self.default_params, "s": "tag"}


class Rule34(BaseClient[httpx.Client]):
    _client: httpx.Client

    def __init__(self) -> None:
        super().__init__()
        self._client = httpx.Client(base_url=self._base_url)

    def close(self) -> None:
        if hasattr(self, "_client"):
            self._client.close()

    def __del__(self) -> None:
        self.close()

    def __enter__(self) -> "Rule34":
        return self

    def __exit__(self, *args) -> None:
        self.close()

    def search(
        self,
        tags: str,
        *,
        limit: Union[int, None] = None,
        page: Union[int, None] = None,
    ) -> List[Post]:
        params = self._build_params(
            self.post_params, {"tags": tags, "limit": limit, "pid": page}
        )
        request = self._build_request("GET", params)
        response = self._client.send(request)

        if data := response.json():
            return [Post.from_dict(item) for item in data]

        raise NotImplementedError("Failed to search posts")

    def get_post(self, post_id: int) -> Post:
        params = self._build_params(self.post_params, {"id": post_id})
        request = self._build_request("GET", params)
        response = self._client.send(request)

        if data := response.json():
            return Post.from_dict(data.pop())

        raise NotImplementedError("Failed to get post")

    def get_comments(self, post_id: int) -> List[Comment]:
        params = self._build_params(self.comment_params, {"post_id": post_id})
        request = self._build_request("GET", params)
        response = self._client.send(request)

        if xml_content := response.text:
            return XMLParser.parse_comments(xml_content)

        raise NotImplementedError("Failed to get comments")

    def get_random_post(self) -> Post:
        request = self._build_request("GET", self.post_params)
        response = self._client.send(request)

        if data := response.json():
            return Post.from_dict(random.choice(data))

        raise NotImplementedError("Failed to get random post")

    def get_tags(self, *, tag_id: Union[int, None] = None) -> List[Tag]:
        params = {**self.tag_params, "id": tag_id}
        request = self._build_request("GET", params)
        response = self._client.send(request)

        if xml_content := response.text:
            return XMLParser.parse_tags(xml_content)

        raise NotImplementedError("Failed to get tags")


class AsyncRule34(BaseClient[httpx.AsyncClient]):
    _client: httpx.AsyncClient

    def __init__(self) -> None:
        super().__init__()
        self._client = httpx.AsyncClient(base_url=self._base_url)

    async def close(self) -> None:
        if hasattr(self, "_client"):
            await self._client.aclose()

    async def __del__(self) -> None:
        await self.close()

    async def __aenter__(self) -> "Rule34":
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()

    async def search(
        self,
        tags: str,
        *,
        limit: Union[int, None] = None,
        page: Union[int, None] = None,
    ) -> List[Post]:
        params = self._build_params(
            self.post_params, {"tags": tags, "limit": limit, "pid": page},
        )
        request = self._build_request("GET", params)
        response = await self._client.send(request)

        if data := response.json():
            return [Post.from_dict(item) for item in data]

        raise NotImplementedError("Failed to search posts")

    async def get_post(self, post_id: int) -> Post:
        params = self._build_params(self.post_params, {"id": post_id})
        request = self._build_request("GET", params)
        response = await self._client.send(request)

        if data := response.json():
            return Post.from_dict(data.pop())

        raise NotImplementedError("Failed to get post")

    async def get_comments(self, post_id: int) -> List[Comment]:
        params = self._build_params(self.comment_params, {"post_id": post_id})
        request = self._build_request("GET", params)
        response = await self._client.send(request)

        if xml_content := response.text:
            return XMLParser.parse_comments(xml_content)

        raise NotImplementedError("Failed to get comments")

    async def get_random_post(self) -> Post:
        request = self._build_request("GET", self.post_params)
        response = await self._client.send(request)

        if data := response.json():
            return Post.from_dict(random.choice(data))

        raise NotImplementedError("Failed to get random post")

    async def get_tags(self, *, tag_id: Union[int, None] = None) -> List[Tag]:
        params = {**self.tag_params, "id": tag_id}
        request = self._build_request("GET", params)
        response = await self._client.send(request)

        if xml_content := response.text:
            return XMLParser.parse_tags(xml_content)

        raise NotImplementedError("Failed to get tags")
