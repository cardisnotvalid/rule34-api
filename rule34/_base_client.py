from typing import TypeVar, Generic, Union, Dict, Any

import httpx
from httpx import Response, Request, Timeout, URL

from ._constants import DEFAULT_TIMEOUT


HttpxClientT = TypeVar("HttpxClientT", bound=[httpx.Client, httpx.AsyncClient])


class BaseClinet(Generic[HttpxClientT]):
    _client: HttpxClientT
    _base_url: URL
    _timeout: Timeout

    def __init__(self, *, timeout: Union[float, Timeout, None] = None) -> None:
        self._base_url = URL("https://api.rule34.xxx/index.php")
        self._timeout = timeout or DEFAULT_TIMEOUT

    def _format_tags(self, tags: str) -> str:
        return "%20".join("_".join(tag.split()) for tag in tags.split(","))

    def _prepare_params(
        self,
        base_params: Dict[str, str],
        add_params: Dict[str, Any]
    ) -> Dict[str, Any]:
        xparams = {**base_params}
        for key, value in add_params.items():
            if value is not None:
                if key == "tags":
                    value = self._format_tags(value)
                xparams[key] = value
        return xparams

    def _build_request(
        self,
        method: str,
        base_params: Dict[str, str],
        add_params: Dict[str, Any],
    ) -> Request:
        return self._client.build_request(
            method=method,
            url=self.base_url,
            params=self._prepare_params(base_params, add_params)
        )

    @property
    def base_url(self) -> URL:
        return self._base_url

    @base_url.setter
    def base_url(self, url: str) -> None:
        self._base_url = URL(url)

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


class SyncAPIClient(BaseClinet[httpx.Client]):
    _client: httpx.Client

    def __init__(self, *, timeout: Union[float, Timeout, None] = None) -> None:
        super().__init__(timeout=timeout)
        self._client = httpx.Client(base_url=self.base_url, timeout=self._timeout)

    def __enter__(self) -> "SyncAPIClient":
        return self

    def __exit__(self) -> None:
        self.close()

    def close(self) -> None:
        if hasattr(self, "_client"):
            self._client.close()

    def get(self, base_params: Dict[str, str], add_params: Dict[str, Any]) -> Response:
        return self._request("GET", base_params, add_params)

    def post(self, base_params: Dict[str, str], add_params: Dict[str, Any]) -> Response:
        return self._request("POST", base_params, add_params)

    def _request(
        self,
        method: str,
        base_params: Dict[str, str],
        add_params: Dict[str, Any]
    ) -> Response:
        return self._client.send(self._build_request(method, base_params, add_params))


class AsyncAPIClient(BaseClinet[httpx.AsyncClient]):
    _client: httpx.AsyncClient

    def __init__(self, *, timeout: Union[float, Timeout, None] = None) -> None:
        super().__init__(timeout=timeout)
        self._client = httpx.AsyncClient(base_url=self.base_url, timeout=self._timeout)

    async def __aenter__(self) -> "AsyncClient":
        return self

    async def __aexit__(self) -> None:
        await self.close()

    async def close(self) -> None:
        if hasattr(self, "_client"):
            await self._client.aclose()

    async def get(self, base_params: Dict[str, str], add_params: Dict[str, Any]) -> Response:
        return await self._request("GET", base_params, add_params)

    async def post(self, base_params: Dict[str, str], add_params: Dict[str, Any]) -> Response:
        return await self._request("POST", base_params, add_params)

    async def _request(
        self,
        method: str,
        base_params: Dict[str, str],
        add_params: Dict[str, Any]
    ) -> Response:
        return await self._client.send(self._build_request(method, base_params, add_params))
