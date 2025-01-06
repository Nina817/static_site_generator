from textnode import TextNode, TextType

print("hello world")

def main():
    obj = TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev')
    print(obj)

main()
