from text_node_to_html_node import text_node_to_html_node
import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type(self):
        text_node = TextNode('something', TextType.TEXT)
        expected_leaf_node = LeafNode(tag=None, value='something')
        actual_leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(expected_leaf_node, actual_leaf_node)
    
    def test_bold_type(self):
        text_node = TextNode('bold text', TextType.BOLD)
        self.assertEqual(LeafNode(tag='b', value='bold text'), text_node_to_html_node(text_node))
    
    def test_italic_type(self):
        text_node = TextNode('italic text', TextType.ITALIC)
        self.assertEqual(LeafNode(tag='i', value='italic text'), text_node_to_html_node(text_node))

    def test_code_type(self):
        text_node = TextNode('code text', TextType.CODE)
        self.assertEqual(LeafNode(tag='code', value='code text'), text_node_to_html_node(text_node))
    
    def test_links_type(self):
        text_node = TextNode('links text', TextType.LINKS, 'www.something.co.uk')
        self.assertEqual(LeafNode(tag='a', value='links text', props={'href': 'www.something.co.uk'}), text_node_to_html_node(text_node))
    
    def test_images_type(self):
        text_node = TextNode('image', TextType.IMAGES, 'www.something.co.uk')
        self.assertEqual(LeafNode(tag='img', value='', props={'src': 'www.something.co.uk', 'alt':'image'}), text_node_to_html_node(text_node))
