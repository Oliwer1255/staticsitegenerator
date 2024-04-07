import unittest

from extraction import *


class TestExtractionNode(unittest.TestCase):
    def test_image_extraction_eq(self):
        matches = extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")
        self.assertEqual(matches, [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
        ])

    def test_image_extraction_has_no_exclamation(self):
        matches = extract_markdown_images("This is text with an [no !](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)")
        self.assertEqual(matches, [])

    def test_link_extraction_eq(self):
        matches = extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)")
        self.assertEqual(matches, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_link_extraction_has_exclamation(self):
        matches = extract_markdown_links("This is text with a ![link](https://www.example.com) and ![another](https://www.example.com/another)")
        self.assertEqual(matches, [])
        

if __name__ == "__main__":
    unittest.main()