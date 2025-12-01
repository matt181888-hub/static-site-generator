from textnode import *
from htmlnode import *
from split_nodes_delimiter import *
from extract_markdown import *

def split_nodes_links(old_nodes):
    final_list = []
    for item in old_nodes:
        if item.text_type != TextType.TEXT:
            final_list.append(item)
            continue
        string = item.text        
        result = []
        while True:
            link_info = extract_markdown_links(string)
            if not link_info:
                break
            link_text, link_url = link_info[0]  
            spliced = string.split(f"[{link_text}]({link_url})", 1)
            before = spliced[0]
            after = spliced[1]
            if before != "":
                new_text_node = TextNode(f"{before}", TextType.TEXT)
                result.append(new_text_node)
            new_link_node = TextNode(f"{link_text}", TextType.LINK, f"{link_url}")
            result.append(new_link_node)
            string = after
        if string:
            final_text_node = TextNode(f"{string}", TextType.TEXT)
            result.append(final_text_node)
        final_list.extend(result)
    return final_list

def split_nodes_images(old_nodes):
    final_list = []
    for item in old_nodes:
        if item.text_type != TextType.TEXT:
            final_list.append(item)
            continue
        string = item.text        
        result = []
        while True:
            image_info = extract_markdown_images(string)
            if not image_info:
                break
            image_text, image_url = image_info[0]  
            spliced = string.split(f"![{image_text}]({image_url})", 1)
            before = spliced[0]
            after = spliced[1]
            if before != "":
                new_text_node = TextNode(f"{before}", TextType.TEXT)
                result.append(new_text_node)
            new_link_node = TextNode(f"{image_text}", TextType.IMAGE, f"{image_url}")
            result.append(new_link_node)
            string = after
        if string:
            final_text_node = TextNode(f"{string}", TextType.TEXT)
            result.append(final_text_node)
        final_list.extend(result)
    return final_list








