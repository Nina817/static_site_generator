from textnode import TextNode, TextType
from extract_title import generate_page, generate_pages_recursive
import os
import shutil


def delete_dest():
    dest_folder = 'public'
    if os.path.exists(dest_folder):
        for path in os.listdir(dest_folder):
            full_path = os.path.join(dest_folder, path)
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            elif os.path.isfile(full_path):
                os.remove(full_path)

def source_to_dest(source, destination):
    if os.path.isfile(source):
        shutil.copy(source, destination)
    else:
        for item in os.listdir(source):
            full_path_source = os.path.join(source, item)
            if os.path.isfile(full_path_source):
                shutil.copy(full_path_source, destination)
                print(full_path_source)
            elif os.path.isdir(full_path_source):
                new_dest = destination + '/'.join(full_path_source.split('/')[1:])
                os.mkdir(new_dest)
                source_to_dest(full_path_source, new_dest)


    
def main():
    # obj = TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev')
    # print(obj)
    delete_dest()
    source_to_dest('static', 'public/')
    # generate_page('content/index.md', 'template.html', 'public/index.html')
    generate_pages_recursive('content', 'template.html', 'public')

main()
