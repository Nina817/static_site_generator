from split_nodes_delimiter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextType, TextNode
import unittest

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes_1(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        actual = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        self.assertEqual(expected, actual)
    
    def test_text_to_text_nodes_2(self):
        text = 'This is more text in *italic* and **bold** with a `code block` and a [link](www.google.co.uk) and an ![image](www.fake_image.co.uk)'
        actual  = text_to_textnodes(text)
        expected = [
            TextNode('This is more text in ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC),
            TextNode(' and ', TextType.TEXT),
            TextNode('bold', TextType.BOLD),
            TextNode(' with a ', TextType.TEXT),
            TextNode('code block', TextType.CODE),
            TextNode(' and a ', TextType.TEXT),
            TextNode('link', TextType.LINKS, 'www.google.co.uk'),
            TextNode(' and an ', TextType.TEXT),
            TextNode('image', TextType.IMAGES, 'www.fake_image.co.uk')
        ]
        self.assertEqual(actual, expected)

class TestSplitNodesImagesLinks(unittest.TestCase):
    def test_split_nodes_link(self):
        old_node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(split_nodes_link([old_node]), expected_nodes)
    
    def test_split_nodes_link2(self):
        old_node = TextNode("[to a fake website](www.something.co.uk) and another [website](www.somethingelse.co.uk) more text", TextType.TEXT) 
        expected_nodes = [
            TextNode('to a fake website', TextType.LINKS, 'www.something.co.uk'),
            TextNode(' and another ', TextType.TEXT),
            TextNode('website', TextType.LINKS, 'www.somethingelse.co.uk'),
            TextNode(' more text', TextType.TEXT)
        ]
        self.assertEqual(split_nodes_link([old_node]), expected_nodes)
    
    def test_split_nodes_image(self):
        old_node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT
        )
        expected_nodes = [
            TextNode('This is text with a ', TextType.TEXT),
            TextNode('rick roll', TextType.IMAGES, 'https://i.imgur.com/aKaOqIh.gif'),
            TextNode(' and ', TextType.TEXT),
            TextNode('obi wan', TextType.IMAGES, 'https://i.imgur.com/fJRm4Vk.jpeg')
        ]
        self.assertEqual(split_nodes_image([old_node]), expected_nodes)
    
    def test_split_nodes_link3(self):
        old_node = TextNode("Text with a link to google [to google](www.google.co.uk)", TextType.TEXT)
        expected_nodes = [
            TextNode('Text with a link to google ', TextType.TEXT),
            TextNode('to google', TextType.LINKS, 'www.google.co.uk')
        ]
        self.assertEqual(split_nodes_link([old_node]), expected_nodes)
    
    def test_split_nodes_image2(self):
        old_node = TextNode("This is some text with an image ![fake image](www.fake_image.co.uk)", TextType.TEXT)
        expected_nodes = [
            TextNode('This is some text with an image ', TextType.TEXT),
            TextNode('fake image', TextType.IMAGES, 'www.fake_image.co.uk')
        ]

class TestExtractMarkdownImagesLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]) 

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]) 

    def test_extract_markdown_images_2(self):
        text = "This is some text with an image ![fake image](www.fake_image.co.uk)"
        self.assertEqual(extract_markdown_images(text), [('fake image', 'www.fake_image.co.uk')])
    
    def test_extract_markdown_links_2(self):
        text = "Text with a link to google [to google](www.google.co.uk)"
        self.assertEqual(extract_markdown_links(text), [('to google', 'www.google.co.uk')])
    
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_bold(self):
        node = TextNode('This is text with a **bolded phrase** in the middle', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_multiple_inline_code(self):
        node = TextNode("This is text with a `code block` word and another `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word and another ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_multiple_nodes(self):
        old_nodes = [
            TextNode("This is a `code block`", TextType.TEXT),
            TextNode("Some more text **and bold**", TextType.TEXT),
            TextNode("Regular text", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, '`', TextType.CODE)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("", TextType.TEXT),     
            TextNode("Some more text **and bold**", TextType.TEXT),
            TextNode("Regular text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_no_closing_delimiter(self):
        old_nodes = [TextNode('this is a `code', TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, '`', TextType.CODE)
