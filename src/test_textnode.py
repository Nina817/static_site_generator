import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_type(self):
        node = TextNode('Testing', TextType.ITALIC, url='www.something.com')
        self.assertEqual(node.text_type.value, 'italic text')
    
    def test_no_url(self):
        node  = TextNode('Testing2', TextType.IMAGES)
        self.assertEqual(node.url, None)
    
    def test_not_equal(self):
        node = TextNode('Something', TextType.CODE, url='www.something.co.uk')
        node2 = TextNode('Something 2', TextType.TEXT, url='www.somethingelse.co.uk')
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()