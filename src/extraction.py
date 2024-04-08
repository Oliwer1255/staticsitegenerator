import re

from textnode import *

def markdown_to_blocks(markdown):
    blocks = []

    for block in markdown.split("\n\n"):
        block.strip(" ")
        blocks.append(block)

    return blocks

def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT, None)]
    new_nodes = split_nodes_delimiter(text_node, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        sections = node.text.split(delimiter)

        if(len(sections) % 2 == 0):
            raise Exception("No closing delimiter found")

        i = 0
        for section in sections:
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))
                
            i += 1

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_images(node.text)

        if len(matches) == 0:
            new_nodes.append(node)
            continue

        next_string = node.text
        for i in range(0, len(matches)):
            strings = next_string.split(f"![{matches[i][0]}]({matches[i][1]})", 1)

            if strings[0] != "":
                new_nodes.append(TextNode(strings[0], TextType.TEXT))
            new_nodes.append(TextNode(matches[i][0], TextType.IMAGE, matches[i][1]))
            if len(matches) - 1 == i:
                if strings[1] != "":
                    new_nodes.append(TextNode(strings[1], TextType.TEXT))
            else:
                next_string = strings[1]

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_links(node.text)

        if len(matches) == 0:
            new_nodes.append(node)
            continue

        next_string = node.text
        for i in range(0, len(matches)):
            strings = next_string.split(f"[{matches[i][0]}]({matches[i][1]})", 1)

            if strings[0] != "":
                new_nodes.append(TextNode(strings[0], TextType.TEXT))
            new_nodes.append(TextNode(matches[i][0], TextType.LINK, matches[i][1]))
            if len(matches) - 1 == i:
                if strings[1] != "":
                    new_nodes.append(TextNode(strings[1], TextType.TEXT))
            else:
                next_string = strings[1]

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)