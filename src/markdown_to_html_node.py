from block_to_block_type import *
from text_to_textnodes import *
from split_nodes_delimiter import *
from split_nodes_images_links import *
from textnode import *
from htmlnode import *

def markdown_to_html_node(block_text):
    block_text_list = markdown_to_blocks(block_text)
    nodes = []
    for block in block_text_list:
        block_type = block_to_block_type(block)
        block_tag = block_type_to_node_tag(block_type, block)
        cleaned_text = markdown_cleanup(block, block_type)
        if block_type == BlockType.ordered_list:
            lines = cleaned_text.split("\n")
            all_children = []
            for line in lines:
                child_list = text_to_children(line)
                li_node = ParentNode(tag = "li", children=child_list)
                all_children.append(li_node)
            new_node = ParentNode(tag = block_tag, children=all_children)
        elif block_type == BlockType.unordered_list:
            lines = cleaned_text.split("\n")
            all_children = []
            for line in lines:
                child_list = text_to_children(line)
                li_node = ParentNode(tag = "li", children=child_list)
                all_children.append(li_node)
            new_node = ParentNode(tag = block_tag, children=all_children)
        elif block_type == BlockType.code:
            code_node = LeafNode(tag = block_tag, value = cleaned_text)
            new_node = ParentNode(tag="pre", children=[code_node])
        else:
            cleaned_text = cleaned_text.replace("\n", " ")
            cleaned_text = " ".join(cleaned_text.split())
            new_node_children = text_to_children(cleaned_text)
            new_node = ParentNode(tag = block_tag, children = new_node_children)
        nodes.append(new_node)
    return ParentNode(tag="div", children=nodes)
    



def block_type_to_node_tag(block, block_text = None):
    if block == BlockType.paragraph:
        return "p"
    if block == BlockType.quote:
        return "blockquote"
    if block == BlockType.heading:
        if block_text:
            if block_text[0:6] == "######":
                return "h6"
            
            elif block_text[0:5] == "#####":
                return "h5"
            
            elif block_text[0:4] == "####":
                return "h4"

            elif block_text[0:3] == "###":
                return "h3"

            elif block_text[0:2] == "##":
                return "h2"

            elif block_text[0] == "#":
                return "h1"
    if block == BlockType.code:
        return "code"
    if block == BlockType.unordered_list:
        return "ul"
    if block == BlockType.ordered_list:
        return "ol"
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    list_html_nodes = []
    for node in text_nodes:
        list_html_nodes.append(text_node_to_html_node(node))
    return list_html_nodes
    
def markdown_cleanup(text, block_type):
    if block_type == BlockType.code:
        line_list = text.split("\n")
        correct = []
        for line in line_list:
            keeping = line.lstrip("```")
            correct.append(keeping)
        string = "\n".join(correct)
        return string
    
    if block_type == BlockType.heading:
        new_text = text.lstrip("#")
        return new_text.lstrip()
    
    if block_type == BlockType.quote:
        line_list = text.split("\n")
        correct = []
        for line in line_list:
            if line.startswith("> "):
                keeping = line[2:]
                correct.append(keeping)
            elif line.startswith(">"):
                keeping = line[1:]
                correct.append(keeping)
        string = "\n".join(correct)
        return string
    
    if block_type == BlockType.unordered_list:
        line_list = text.split("\n")
        correct = []
        for line in line_list:
            if line.startswith("- "):
                keeping = line[2:]
                correct.append(keeping)
            elif line.startswith("-"):
                keeping = line[1:]
                correct.append(keeping)
        string = "\n".join(correct)
        return string
    
    if block_type == BlockType.ordered_list:
        line_list = text.split("\n")
        correct = []
        for line in line_list:
            removable = line.split(". ", 1)
            keeping = removable[1]
            correct.append(keeping)
        string = "\n".join(correct)
        return string

    return text
        



    
 
    