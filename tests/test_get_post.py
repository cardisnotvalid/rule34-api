import pytest
import respx

from rule34._models import Post


POST_CONTENT = [{
    "preview_url": "test_preview_url",
    "sample_url": "test_sample_url",
    "file_url": "test_file_url",
    "directory": 1,
    "hash": "test_hash",
    "width": 2,
    "height": 3,
    "id": 4,
    "image": "test_image",
    "change": 5,
    "owner": "test_owner",
    "parent_id": 6,
    "rating": "test_rating",
    "sample": True,
    "sample_width": 7,
    "sample_height": 8,
    "score": 9,
    "tags": "test_tag",
    "source": "test_source",
    "status": "test_status",
    "has_notes": True,
    "comment_count": 10
}]


@respx.mock
def test_get_post(sync_client, respx_mock):
    params = {"page": "dapi", "q": "index", "s": "post", "id": 1}
    respx_mock.get("/index.php", params=params).respond(200, json=POST_CONTENT)

    result = sync_client.get_post(1)
    assert isinstance(result, Post)
    assert result.preview_url == "test_preview_url"
    assert result.sample_url == "test_sample_url"
    assert result.file_url == "test_file_url"
    assert result.directory == 1
    assert result.hash == "test_hash"
    assert result.width == 2
    assert result.height == 3
    assert result.id == 4
    assert result.image == "test_image"
    assert result.change == 5
    assert result.owner == "test_owner"
    assert result.parent_id == 6
    assert result.rating == "test_rating"
    assert result.sample == True
    assert result.sample_width == 7
    assert result.sample_height == 8
    assert result.score == 9
    assert result.tags == "test_tag"
    assert result.source == "test_source"
    assert result.status == "test_status"
    assert result.has_notes == True
    assert result.comment_count == 10


@pytest.mark.asyncio
@respx.mock
async def test_async_get_post(async_client, respx_mock):
    params = {"page": "dapi", "q": "index", "s": "post", "id": 1}
    respx_mock.get("/index.php", params=params).respond(200, json=POST_CONTENT)

    result = await async_client.get_post(1)
    assert isinstance(result, Post)
    assert result.preview_url == "test_preview_url"
    assert result.sample_url == "test_sample_url"
    assert result.file_url == "test_file_url"
    assert result.directory == 1
    assert result.hash == "test_hash"
    assert result.width == 2
    assert result.height == 3
    assert result.id == 4
    assert result.image == "test_image"
    assert result.change == 5
    assert result.owner == "test_owner"
    assert result.parent_id == 6
    assert result.rating == "test_rating"
    assert result.sample == True
    assert result.sample_width == 7
    assert result.sample_height == 8
    assert result.score == 9
    assert result.tags == "test_tag"
    assert result.source == "test_source"
    assert result.status == "test_status"
    assert result.has_notes == True
    assert result.comment_count == 10
