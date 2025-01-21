import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import ParentNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_markdown_to_html_node1(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

```
This is a code block.
```

1. Item 1
2. Item 2
3. Item 3

> This is a quote."""
        actual = markdown_to_html_node(markdown)
        expected = ParentNode(tag ='div', children=[
                                ParentNode(tag = 'h1', children=[LeafNode(tag=None, value='This is a heading')]),
                                ParentNode(tag='p', children=[
                                    LeafNode(tag=None, value='This is a paragraph of text. It has some '),
                                    LeafNode(tag='b', value='bold'),
                                    LeafNode(tag=None, value=' and '),
                                    LeafNode(tag='i', value='italic'),
                                    LeafNode(tag=None, value=' words inside of it.')
                                ]),
                                ParentNode(tag='ul', children=[
                                    ParentNode(tag='li', children= [
                                        LeafNode(tag=None, value='This is the first list item in a list block')
                                    ]),
                                    ParentNode(tag='li', children=[
                                        LeafNode(tag=None, value = 'This is a list item')
                                    ]),
                                    ParentNode(tag='li', children=[
                                        LeafNode(tag=None, value='This is another list item')
                                    ]),
                                ]),
                                ParentNode(tag='code', children=[
                                        LeafNode(tag=None, value='This is a code block.')
                                ]),
                                ParentNode(tag = 'ol', children=[
                                    ParentNode(tag='li', children=[
                                        LeafNode(tag=None, value='Item 1')
                                    ]),
                                    ParentNode(tag='li', children=[
                                        LeafNode(tag=None, value='Item 2')
                                    ]),
                                    ParentNode(tag='li', children=[
                                        LeafNode(tag=None, value='Item 3')
                                    ])
                                ]),
                                ParentNode(tag='blockquote', children=[LeafNode(tag=None, value='This is a quote.')])
                                
                            ])
        self.assertEqual(actual, expected)
    
    def test_markdown_to_html_node2(self):
        markdown = '''###### This is a small heading

        This is a paragraph of **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
        '''
        actual = markdown_to_html_node(markdown)
        expected = ParentNode('div', children=[
            ParentNode(tag='h6', children=[LeafNode(tag=None, value='This is a small heading')]),
            ParentNode(tag='p', children=[
                LeafNode(tag=None, value='This is a paragraph of '),
                LeafNode(tag='b', value='text'),
                LeafNode(tag=None, value=' with an '),
                LeafNode(tag='i', value='italic'),
                LeafNode(tag=None, value=' word and a '),
                LeafNode(tag='code', value='code block'),
                LeafNode(tag=None, value=' and an '),
                LeafNode(tag='img', value='', props={'src':'https://i.imgur.com/fJRm4Vk.jpeg', 'alt':'obi wan image'}),
                LeafNode(tag=None, value=' and a '),
                LeafNode(tag='a', value='link', props={'href':'https://boot.dev'})
            ])
        ])
        self.assertEqual(actual, expected)