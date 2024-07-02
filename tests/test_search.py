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
def test_search(sync_client, respx_mock):
    params = {
        "page": "dapi",
        "q": "index",
        "s": "post",
        "json": 1,
        "tags": "test_tag",
        "limit": 1,
        "pid": 1
    }
    respx_mock.get("/index.php", params=params).respond(200, json=POST_CONTENT)

    result = sync_client.search("test tag", limit=1, page=1)
    assert isinstance(result, list)

    post = result[0]
    assert post.preview_url == "test_preview_url"
    assert post.sample_url == "test_sample_url"
    assert post.file_url == "test_file_url"
    assert post.directory == 1
    assert post.hash == "test_hash"
    assert post.width == 2
    assert post.height == 3
    assert post.id == 4
    assert post.image == "test_image"
    assert post.change == 5
    assert post.owner == "test_owner"
    assert post.parent_id == 6
    assert post.rating == "test_rating"
    assert post.sample == True
    assert post.sample_width == 7
    assert post.sample_height == 8
    assert post.score == 9
    assert post.tags == "test_tag"
    assert post.source == "test_source"
    assert post.status == "test_status"
    assert post.has_notes == True
    assert post.comment_count == 10


@pytest.mark.asyncio
@respx.mock
async def test_async_search(async_client, respx_mock):
    params = {
        "page": "dapi",
        "q": "index",
        "s": "post",
        "json": 1,
        "tags": "test_tag",
        "limit": 1,
        "pid": 1
    }
    respx_mock.get("/index.php", params=params).respond(200, json=POST_CONTENT)

    result = await async_client.search("test tag", limit=1, page=1)
    assert isinstance(result, list)

    post = result[0]
    assert post.preview_url == "test_preview_url"
    assert post.sample_url == "test_sample_url"
    assert post.file_url == "test_file_url"
    assert post.directory == 1
    assert post.hash == "test_hash"
    assert post.width == 2
    assert post.height == 3
    assert post.id == 4
    assert post.image == "test_image"
    assert post.change == 5
    assert post.owner == "test_owner"
    assert post.parent_id == 6
    assert post.rating == "test_rating"
    assert post.sample == True
    assert post.sample_width == 7
    assert post.sample_height == 8
    assert post.score == 9
    assert post.tags == "test_tag"
    assert post.source == "test_source"
    assert post.status == "test_status"
    assert post.has_notes == True
    assert post.comment_count == 10
