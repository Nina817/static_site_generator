import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        actual = block_to_block_type('# This is a heading')
        expected = 'HEADING'
        self.assertEqual(actual, expected)
    
    def test_paragraph(self):
        actual = block_to_block_type('This is a paragraph of text.')
        expected = 'PARAGRAPH'
        self.assertEqual(actual, expected)
    
    def test_unordered_list(self):
        text = """* This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        actual = block_to_block_type(text)
        expected = 'UNORDERED_LIST'
        self.assertEqual(actual, expected)
    
    def test_ordered_list(self):
        text = """1. Item 1
        2. Item 2
        3. Item 3"""
        actual = block_to_block_type(text)
        expected = 'ORDERED_LIST'
        self.assertEqual(actual, expected)
    
    def test_quote(self):
        actual = block_to_block_type('> This is a quote.')
        expected = 'QUOTE'
        self.assertEqual(actual, expected)

    def test_code(self):
        text = """```
        This is code
        ```"""
        actual = block_to_block_type(text)
        expected = 'CODE'
        self.assertEqual(actual, expected)

        

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_1(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        actual = markdown_to_blocks(markdown)
        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', """* This is the first list item in a list block
        * This is a list item
        * This is another list item"""]
        self.assertEqual(actual, expected)
    
    def test_markdown_to_blocks_2(self):
        markdown = """1. Item 1\n2. Item 2\n3. Item 3\n\n> This is a quote.\n\n![alt text for image](url/of/image.jpg)"""
        actual = markdown_to_blocks(markdown)
        expected = ["""1. Item 1\n2. Item 2\n3. Item 3""", "> This is a quote.", "![alt text for image](url/of/image.jpg)"]
        self.assertEqual(expected, actual)