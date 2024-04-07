import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):

    #HTMLNode tests
    def test_eq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')   

    def test_not_eq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target trew": "_blank"})
        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"') 


    #LeafNode tests
    def test_leaf_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>') 

    def test_leaf_exception(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_raw(self):
        node = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Click me!") 


    #ParentNode tests
    def test_parent_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>') 

    def test_parent_no_children(self):
        node = ParentNode(
            "p",
            [],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_nesting_eq(self):
        node = ParentNode(
            "p",
            [
                ParentNode("p", [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><p>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>') 

    

if __name__ == "__main__":
    unittest.main()