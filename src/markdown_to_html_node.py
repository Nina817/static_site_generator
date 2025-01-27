from markdown_to_blocks import *
from htmlnode import *
from split_nodes_delimiter import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
    for node in html_nodes:
        if not node.value:
            print(node)
    return html_nodes

def list_to_list_nodes(block):
    list_nodes = []
    list_items = [item.split(' ', 1)[1] for item in block.split('\n')]
    for text in list_items:
        list_nodes.append(ParentNode('li', text_to_children(text)))
    return list_nodes

def block_to_HTMLNode(block):
    block_type = block_to_block_type(block)
    if block_type == 'PARAGRAPH':
        return ParentNode('p', text_to_children(block))
    if block_type == 'CODE':
        value = block.replace('```\n', '')
        value = value.replace('\n```', '')
        return ParentNode('code', text_to_children(value))
    if block_type == 'HEADING':
        block_list = block.split(' ', 1)
        return ParentNode(f"h{len(block_list[0])}", text_to_children(block_list[1]))
    if block_type == 'QUOTE':
        return ParentNode('blockquote', text_to_children(block.replace('> ', '')))
    if block_type == 'ORDERED_LIST':
        return ParentNode('ol', list_to_list_nodes(block))
    if block_type == 'UNORDERED_LIST':
        return ParentNode('ul', list_to_list_nodes(block))
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    HTMLNodes = []
    for block in blocks:
        HTMLNodes.append(block_to_HTMLNode(block))
    return ParentNode('div', HTMLNodes)
    






