from rule34._client import BaseClient


def test_build_params() -> None:
    base_client = BaseClient()
    base_params = {"page": "dapi", "q": "index"}
    add_params = {"json": 1, "tags": "tag one, tag two, tag three", "limit": 10}
    expected = {
        "page": "dapi",
        "q": "index",
        "json": 1,
        "tags": "tag_one%20tag_two%20tag_three",
        "limit": 10
    }
    assert base_client._build_params(base_params, add_params) == expected

