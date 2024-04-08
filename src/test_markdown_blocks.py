import unittest

from markdown_blocks import *


class TestExtractionNode(unittest.TestCase):

    def test_markdown_to_blocks_1(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "This is **bolded** paragraph", 
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line"
        ])

    def test_markdown_to_blocks_2(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "This is **bolded** paragraph", 
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            """* This is a list\n* with items"""

        ])

    def test_block_to_type_paragraph(self):
        block = "This is just text"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_type_heading_1(self):
        block = "# heading 1\n test"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_block_to_type_heading_4(self):
        block = "#### heading 4\n test"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_type_code(self):
        block = "```This is just code\nsdsddss```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_type_quote(self):
        block = "> This is just a quote\n> sdsddss"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_type_unordered_list(self):
        block = "* This is just a unordered list\n- sdsddss"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_type_unordered_list(self):
        block = "1. This is just a ordered list\n2. sdsddss"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_type_return_paragraph(self):
        block = "1. This is just a ordered list\n3. sdsddss"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()