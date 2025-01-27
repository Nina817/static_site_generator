from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes:list, delimiter, text_type:TextType):
    result = []
    for j in range(len(old_nodes)):
        node = old_nodes[j]
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            value_list = node.text.split(delimiter)
            if len(value_list) %2 == 0:
                raise Exception('No closing delimiter')
            else:
                for i in range(len(value_list)):
                    text = value_list[i]
                    if text:
                        if i == len(value_list)-1 and not text and j==len(old_nodes)-1:
                            continue
                        if i%2 !=0: # if is inline text e.g. code block
                            result.append(TextNode(text, text_type))
                        else:
                            result.append(TextNode(text, TextType.TEXT))
    return result

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
        else:
            text = node.text
            for link in links:
                text_list = text.split(f"[{link[0]}]({link[1]})", 1)
                if text_list[0]:
                    result.append(TextNode(text_list[0], TextType.TEXT))
                link_node = TextNode(link[0], TextType.LINKS, link[1])
                result.append(link_node)
                text = text_list[1]
            if text:
                result.append(TextNode(text, TextType.TEXT))
    return result

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
        else:
            text = node.text
            for image in images:
                text_list = text.split(f"![{image[0]}]({image[1]})", 1)
                if text_list[0]:
                    result.append(TextNode(text_list[0], TextType.TEXT))
                image_node = TextNode(image[0], TextType.IMAGES, image[1])
                result.append(image_node)
                text = text_list[1]
            if text:
                result.append(TextNode(text, TextType.TEXT))
    return result

def text_to_textnodes(text):
    input_nodes = [TextNode(text, TextType.TEXT)]
    for item in [(TextType.BOLD, '**'), (TextType.CODE, '`'), (TextType.ITALIC, '*')]:
        input_nodes = split_nodes_delimiter(input_nodes, item[1], item[0])
    extracted_links = split_nodes_link(input_nodes)
    extracted_images_and_links = split_nodes_image(extracted_links)
    return extracted_images_and_links
