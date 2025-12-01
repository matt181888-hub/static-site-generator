from textnode import *
from htmlnode import *
from split_nodes_delimiter import *
from extract_markdown import *
from split_nodes_images_links import *

def text_to_textnodes(text):
    node = [TextNode(f"{text}", TextType.TEXT)]
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    node = split_nodes_images(node)
    node = split_nodes_links(node)
    return node

