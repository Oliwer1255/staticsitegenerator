import unittest

from textnode import *
from extraction import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_link(self):
        node = TextNode("This is a text node", TextType.BOLD, "link")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)    

    def test_not_eq_text(self):
        node = TextNode("This is a text node 3232", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_split_text_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    
        

if __name__ == "__main__":
    unittest.main()