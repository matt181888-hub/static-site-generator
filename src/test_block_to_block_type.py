import unittest
from markdown_to_blocks import *
from block_to_block_type import *

class BlockToBlockType(unittest.TestCase):
    def test_one(self):
        md = "2 This is **bolded** paragraph"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.paragraph, block_type)
    
    def test_two(self):
        md = "``` this is code```"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.code, block_type)

    def test_three_heading_with_max_level(self):
        md = "###### This is level 6 heading"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.heading, block_type)

    def test_four_heading_invalid_no_space_after_number(self):
        md = "2This should NOT be a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.paragraph, block_type)

    def test_five_code_block_with_extra_content_outside_backticks(self):
        md = "```code with backticks```   "
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.code, block_type)

    def test_six_code_block_missing_closing_backticks(self):
        md = "``` missing end"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.paragraph, block_type)

    def test_seven_quote_block_detection(self):
        md = """> this is a quote bloc 
>this is also a quote
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.quote, block_type)

    def test_eight_unordered_list_edge_case_multiple_dashes(self):
        md = "-- Not actually a list"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.paragraph, block_type)

    def test_nine_ordered_list_single_digit(self):
        md = """1. first list item
2. hellow
3. hellow
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.ordered_list, block_type)

    def test_ten_ordered_list_not_sequential(self):
        md = """1. first item
1. second item
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.paragraph, block_type)

    def test_eleven_heading_with_max_level(self):
        md = "# This is level 1 heading"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.heading, block_type)

    def test_twelve_heading_with_max_level(self):
        md = "#This is level 1 heading"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.paragraph, block_type)



