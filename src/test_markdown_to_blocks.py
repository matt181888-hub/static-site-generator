import unittest
from markdown_to_blocks import *

class UnitTestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        def test_split_single_paragraph_with_markdown_formats(self):
            md = """
This is a **bold** paragraph with some _italic_ text and also `code` inside.
Still the same paragraph on a new line.
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a **bold** paragraph with some _italic_ text and also `code` inside.\nStill the same paragraph on a new line."
                ],
            )

        def test_split_multiple_paragraphs_each_with_markdown_formats(self):
            md = """
First **bold** paragraph.

Second paragraph has _italic_ elements.

Third one includes some `code` examples.
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "First **bold** paragraph.",
                    "Second paragraph has _italic_ elements.",
                    "Third one includes some `code` examples.",
                ],
            )

        def test_ignores_extra_whitespace_but_keeps_markdown_in_text(self):
            md = """


Here is a paragraph with **bold**, _italic_, and `code` despite blank lines above.



"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "Here is a paragraph with **bold**, _italic_, and `code` despite blank lines above.",
                ],
            )

        def test_handles_list_blocks_preserving_markdown_formats(self):
            md = """
- **bold item**
- _italic item_
- `code item`

1. **bold number**
2. _italic number_
3. `code number`
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "- **bold item**\n- _italic item_\n- `code item`",
                    "1. **bold number**\n2. _italic number_\n3. `code number`",
                ],
            )
