from rule34._client import BaseClient


def test_prepare_params():
    base_client = BaseClient()
    params = {"tags": "tag one, tag two", "limit": None, "json": 1}
    expected = {"tags": "tag_one%20tag_two", "json": 1}
    assert base_client._prepare_params(params) == expected
