from textnode import *
from htmlnode import *
from split_nodes_delimiter import *
from extract_markdown import *
from split_nodes_images_links import *
import unittest
from text_to_textnodes import *

class TestTextToTextnodes(unittest.TestCase):

    def test_one(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertEqual([
                            TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with an ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" word and a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" and an ", TextType.TEXT),
                            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.TEXT),
                            TextNode("link", TextType.LINK, "https://boot.dev"),
                            ], result)

    def test_2_converts_plain_text_without_markdown_into_single_textnode(self):
        result = text_to_textnodes("hello world")
        expected = [TextNode("hello world", TextType.TEXT)]
        self.assertListEqual(result, expected)

    def test_3_splits_bold_markdown_into_separate_nodes(self):
        result = text_to_textnodes("this is **bold** text")
        expected = [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_4_splits_italic_markdown_into_separate_nodes(self):
        result = text_to_textnodes("a _cool_ word")
        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("cool", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_5_splits_code_markdown_into_separate_nodes(self):
        result = text_to_textnodes("run `this` now")
        expected = [
            TextNode("run ", TextType.TEXT),
            TextNode("this", TextType.CODE),
            TextNode(" now", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_6_identifies_image_markdown_into_image_node(self):
        result = text_to_textnodes("look ![alt text](https://img.com/x.png) here")
        expected = [
            TextNode("look ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://img.com/x.png"),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_7_identifies_link_markdown_into_link_node(self):
        result = text_to_textnodes("visit [site](https://example.com) now")
        expected = [
            TextNode("visit ", TextType.TEXT),
            TextNode("site", TextType.LINK, "https://example.com"),
            TextNode(" now", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_8_correctly_processes_multiple_markdown_types_in_one_string(self):
        text = "a **bold** _italic_ `code`"
        result = text_to_textnodes(text)
        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertListEqual(result, expected)

    def test_9_parses_nested_or_adjacent_markdown_sequences_correctly(self):
        result = text_to_textnodes("**bold**_italic_`code`")
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code", TextType.CODE),
        ]
        self.assertListEqual(result, expected)

    def test_10_matches_full_example_from_prompt_with_all_markdown_types(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a "
            "[link](https://boot.dev)"
        )

        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(result, expected)

