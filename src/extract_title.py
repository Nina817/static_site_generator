
from markdown_to_blocks import *
from markdown_to_html_node import markdown_to_html_node
from pprint import pprint
import os

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    try:
        header = [block for block in blocks if block.startswith('# ')][0]
    except:
        raise Exception('No h1 header')
    return header.split(' ', 1)[1]

def generate_page(from_path, template_path, dest_path):
    print('Generating page from from_path to dest_pat using template_path')
    markdown_file = open(from_path, 'r')
    markdown = markdown_file.read()
    title = extract_title(markdown)
    template_file= open(template_path, 'r')
    template = template_file.read()
    html_nodes = markdown_to_html_node(markdown)
    html= html_nodes.to_html()
    markdown_file.close()
    template_file.close()
    content_template = template.replace('{{ Content }}', html)
    final_template = content_template.replace('{{ Title }}', title)
    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    index_file = open(dest_path, 'w')
    index_file.write(final_template)
    index_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        dest_dir_path = dest_dir_path.replace('.md', '.html')
        generate_page(dir_path_content, template_path, dest_dir_path)
    else:
        for item in os.listdir(dir_path_content):
            full_path_source = os.path.join(dir_path_content, item)
            full_path_dest = os.path.join(dest_dir_path, item)
            generate_pages_recursive(full_path_source, template_path, full_path_dest)

# generate_pages_recursive('content', 'template.html', 'public')

