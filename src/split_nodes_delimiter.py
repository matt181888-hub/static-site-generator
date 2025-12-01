from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_list = []
    for item in old_nodes:
        if item.text_type != TextType.TEXT:
            final_list.append(item)
            continue
        string = item.text
        seperated_sring = string.split(delimiter)
        length = len(seperated_sring)
        if length % 2 == 0:
            raise Exception("Error: Incorrect Markdown syntax")
        else:
            for i, msg in enumerate(seperated_sring):
                if msg == "":
                    continue
                if i % 2 == 0:
                    new_txt_node = TextNode(msg, TextType.TEXT)
                    final_list.append(new_txt_node)
                if i % 2 != 0:
                    new_delimiter_node = TextNode(msg, text_type)
                    final_list.append(new_delimiter_node)

    return final_list



        
        
            
