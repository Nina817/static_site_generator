from enum import Enum

class BlockType(Enum):
    HEADING = '#'
    CODE = '```'
    QUOTE = '> '
    UNORDERED_LIST = ('- ', '* ')
    ORDERED_LIST = '1. '

def markdown_to_blocks(markdown):
    blocks= markdown.split('\n\n')
    return [block.strip() for block in blocks if block]

def block_to_block_type(markdown_block):
    result = ''
    for markdown_type in BlockType:
        if markdown_block.startswith(markdown_type.value):
            result= markdown_type.name
    if not result:
        result = 'PARAGRAPH'
    return result


