from rule34._client import BaseClient


def test_format_tags():
    base_client = BaseClient()
    assert base_client._format_tags("tag one, tag two") == "tag_one%20tag_two"
