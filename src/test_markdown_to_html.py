import unittest

from markdown_to_html import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_eq_1(self):
        document = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""
        node = markdown_to_html_node(document)
        self.assertEqual(node.to_html(), "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is a list item</li><li>This is another list item</li></ul></div>")

    def test_eq_quote(self):
        document = """> quotes
> quotes
> quotes"""
        node = markdown_to_html_node(document)
        self.assertEqual(node.to_html(), "<div><blockquote>quotes\nquotes\nquotes</blockquote></div>")

    def test_eq_image(self):
        document = """Just a paragraph with a ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"""
        node = markdown_to_html_node(document)
        self.assertEqual(node.to_html(), '<div><p>Just a paragraph with a <img src="https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png" alt="image"></img></p></div>')

    def test_eq_link(self):
        document = """Just a paragraph with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"""
        node = markdown_to_html_node(document)
        self.assertEqual(node.to_html(), '<div><p>Just a paragraph with a <a href="https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png">link</a></p></div>')
        

if __name__ == "__main__":
    unittest.main()