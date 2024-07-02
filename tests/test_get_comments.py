import pytest
import respx

from rule34._models import Comment


XML_CONTENT = """
<?xml version="1.0" encoding="UTF-8"?>
<comments type="array">
    <comment created_at="2024-01-01 15:00" post_id="1" body="test" creator="test" id="2" creator_id="3"/>
</comments>
"""


@respx.mock
def test_get_comments(sync_client, respx_mock):
    params = {"page": "dapi", "q": "index", "s": "comment", "post_id": 1}
    respx_mock.get("/index.php", params=params).respond(200, text=XML_CONTENT)

    result = sync_client.get_comments(1)
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Comment)
    assert result[0].created_at == "2024-01-01 15:00"
    assert result[0].post_id == 1
    assert result[0].body == "test"
    assert result[0].creator == "test"
    assert result[0].id == 2
    assert result[0].creator_id == 3


@pytest.mark.asyncio
@respx.mock
async def test_async_get_comments(async_client, respx_mock):
    params = {"page": "dapi", "q": "index", "s": "comment", "post_id": 1}
    respx_mock.get("/index.php", params=params).respond(200, text=XML_CONTENT)

    result = await async_client.get_comments(1)
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Comment)
    assert result[0].created_at == "2024-01-01 15:00"
    assert result[0].post_id == 1
    assert result[0].body == "test"
    assert result[0].creator == "test"
    assert result[0].id == 2
    assert result[0].creator_id == 3
