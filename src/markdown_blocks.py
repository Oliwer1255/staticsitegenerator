from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1,
    HEADING = 2,
    CODE = 3,
    QUOTE = 4,
    UNORDERED_LIST = 5,
    ORDERED_LIST = 6


def markdown_to_blocks(markdown):
    blocks = []

    for block in markdown.split("\n\n"):
        if block == "":
            continue
        block.strip(" ")
        blocks.append(block)

    return blocks

def block_to_block_type(block):
    

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")

    for i in range(0, len(lines)):
        if not lines[i].startswith(">"):
            break

        if i == len(lines) - 1:
            return BlockType.QUOTE
        
    for i in range(0, len(lines)):
        if not lines[i].startswith("*") and not lines[i].startswith("-"):
            break

        if i == len(lines) - 1:
            return BlockType.UNORDERED_LIST
        
    for i in range(0, len(lines)):
        if not lines[i].startswith(f"{i + 1}."):
            break

        if i == len(lines) - 1:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
