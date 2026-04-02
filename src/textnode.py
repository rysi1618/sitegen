from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text 
                and self.text_type == other.text_type
                and self.url == other.url)
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")
    
def text_node_to_html_node(text_node):
    tag, value, props = None, "", None
    match text_node.text_type:
        case TextType.TEXT:
            value = text_node.text
        case TextType.BOLD:
            tag = "b"
            value = text_node.text
        case TextType.ITALIC:
            tag = "i"
            value = text_node.text
        case TextType.CODE:
            tag = "code"
            value = text_node.text
        case TextType.LINK:
            tag = "a"
            value = text_node.text
            props = {"href": text_node.url}
        case TextType.IMAGE:
            tag = "img"
            props = {"src": text_node.url, "alt": text_node.text}
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")
    return LeafNode(tag, value, props)