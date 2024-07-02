import pytest
import httpx


@pytest.fixture
def sync_client():
    from rule34 import Rule34

    client = Rule34()
    client._client = httpx.Client(base_url=client._base_url)
    return client


@pytest.fixture
def async_client():
    from rule34 import AsyncRule34

    client = AsyncRule34()
    client._client = httpx.AsyncClient(base_url=client._base_url)
    return client
