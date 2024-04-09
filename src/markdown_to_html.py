from markdown_blocks import *
from htmlnode import *
from textnode import *
from extraction import *

def markdown_to_html_node(document):
    blocks = markdown_to_blocks(document)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html(block))
        if block_type == BlockType.HEADING:
            children.append(heading_to_html(block))
        if block_type == BlockType.CODE:
            children.append(code_to_html(block))
        if block_type == BlockType.QUOTE:
            children.append(quote_to_html(block))
        if block_type == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html(block))
        if block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html(block))

    return ParentNode("div", children)


def paragraph_to_html(block):
    text_nodes = text_to_textnodes(block)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return ParentNode("p", children)

def heading_to_html(block):
    tag = ""

    if block.startswith("# "):
        tag = "h1"
    elif block.startswith("## "):
        tag = "h2"
    elif block.startswith("### "):
        tag = "h3"
    elif block.startswith("#### "):
        tag = "h4"
    elif block.startswith("##### "):
        tag = "h5"
    elif block.startswith("###### "):
        tag = "h6"
    else:
        raise Exception("Invalid heading")
    
    block = block.lstrip("# ")
    
    text_nodes = text_to_textnodes(block)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return ParentNode(tag, children)

def code_to_html(block):
    block = block.strip("```")

    return ParentNode("pre", [ParentNode("code", [LeafNode(None, block)])]) 

def quote_to_html(block):
    lines = block.split("\n")
    for i in range(0, len(lines)):
        lines[i] = lines[i].lstrip("> ")

    block = "\n".join(lines)

    text_nodes = text_to_textnodes(block)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return ParentNode("blockquote", children)

def unordered_list_to_html(block):
    lines = block.split("\n")
    children = []

    for line in lines:
        line = line.lstrip("* ")
        line = line.lstrip("- ")
        children.append(LeafNode("li", line))

    return ParentNode("ul", children)

def ordered_list_to_html(block):
    lines = block.split("\n")
    children = []

    for i in range(0, len(lines)):
        lines[i] = lines[i].lstrip(f"{i}. ")
        children.append(LeafNode("li", lines[i]))

    return ParentNode("ol", children)