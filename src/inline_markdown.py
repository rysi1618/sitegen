import re
from textnode import *

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        node = []
        count = old_node.text.count(delimiter)
        type_status = False
        if not old_node.text_type.TEXT or count == 0:
            new_nodes.append(old_node)
            continue
        if count % 2 != 0:
            raise ValueError(f"Text node is missing closing delimiter {delimiter}")
        splits = old_node.text.split(delimiter)
        for s in splits:
            if s != "":
                if type_status:
                    node.append(TextNode(s, text_type))
                else:
                    node.append(TextNode(s, TextType.TEXT))
            type_status = not type_status
        new_nodes.extend(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text_type.TEXT:
            new_nodes.append(old_node)
            continue
        orig_text = old_node.text
        images = extract_markdown_images(orig_text)
        if not images:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = orig_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            orig_text = sections[1]
        if orig_text != "":
            new_nodes.append(TextNode(orig_text, TextType.TEXT))        
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text_type.TEXT:
            new_nodes.append(old_node)
            continue
        orig_text = old_node.text
        links = extract_markdown_links(orig_text)
        if not links:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = orig_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            orig_text = sections[1]
        if orig_text != "":
            new_nodes.append(TextNode(orig_text, TextType.TEXT))        
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
