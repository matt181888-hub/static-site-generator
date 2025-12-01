from enum import Enum
from markdown_to_blocks import * 

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"
def is_integeger(s, min_val = float("-inf"), max_val = float("inf")):
    try:
        num = int(s)
        return min_val <= num <= max_val
    except ValueError:
        return False

def block_to_block_type(md_block):
    md_block = md_block.strip()
    md_list = md_block.split("\n")
    if md_block[0:6] == "######" and md_block[7] == " ":
        return BlockType.heading

    if md_block[0:5] == "#####" and md_block[6] == " ":
        return BlockType.heading

    if md_block[0:4] == "####" and md_block[5] == " ":
        return BlockType.heading

    if md_block[0:3] == "###" and md_block[4] == " ":
        return BlockType.heading

    if md_block[0:2] == "##" and md_block[3] == " ":
        return BlockType.heading

    if md_block[0] == "#" and md_block[1] == " ":
        return BlockType.heading

    if md_block[0:3] == "```" and md_block[-3:] == "```":
        return BlockType.code

    if md_block[0] == ">":
        is_quote = True
        for md in md_list:
            if md[0] != ">":
                is_quote = False
                break
        if is_quote:
            return BlockType.quote
    if md_block[0:2] == "- ":
        is_unordered = True
        for md in md_list:
            if md[0:2] != "- ":
                is_unordered = False
                break
        if is_unordered:
            return BlockType.unordered_list

    if md_block[0:3] == "1. ":
        is_ordered = True
        num = 1
        for md in md_list:
            if md[0:3] != f"{num}. ":
                is_ordered = False
                break
            num += 1
        if is_ordered:
            return BlockType.ordered_list

    return BlockType.paragraph
        
            
