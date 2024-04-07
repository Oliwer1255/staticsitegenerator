from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = 1,
    BOLD = 2,
    ITALIC = 3,
    CODE = 4,
    LINK = 5,
    IMAGE = 6

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})

    raise ValueError("No matching text type found")


