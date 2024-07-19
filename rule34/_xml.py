from typing import List, Dict, Any
from xml.etree import cElementTree
from xml.etree.ElementTree import ElementTree, Element

from ._models import Comment, Tag


class XMLParser:
    @staticmethod
    def parse_comments(xml_content: str) -> List[Comment]:
        tree = cElementTree.fromstring(xml_content.strip())
        result = []

        for element in tree.iter():
            if element.tag == "comment":
                comment = Comment(**element.attrib)
                result.append(comment)

        return result

    @staticmethod
    def parse_tags(xml_content: str) -> List[Tag]:
        tree = cElementTree.fromstring(xml_content.strip())
        result = []

        for element in tree.iter():
            if element.tag == "tag":
                tag = Tag(**element.attrib)
                result.append(tag)

        return result
