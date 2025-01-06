from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node= HTMLNode('p', 'something', ['a', 'li'], {
        "href": "https://www.google.com", 
        "target": "_blank",
        })
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())
    
    def test_tag(self):
        node = HTMLNode('a', 'something else')
        self.assertEqual(node.tag, 'a')
    
    def test_value(self):
        node = HTMLNode(value = 'something else again')
        self.assertEqual(node.value, 'something else again')

    def test_to_html(self):
        node = LeafNode('p', 'This is a paragraph of text.')
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
    
    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html3(self):
        node = LeafNode(None, 'something')
        self.assertEqual(node.to_html(), 'something')
    
    def test_parent_node_to_html(self):
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
    
    def test_parent_node_no_children(self):
        node = ParentNode(
            'p',
            []
        )
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_node_in_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ) 
        node_2  = ParentNode('body', [node])
        self.assertEqual(node_2.to_html(), '<body><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></body>')