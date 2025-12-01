import unittest
from textnode import *
from htmlnode import *
from split_nodes_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delimiter_one(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,correct)
    
    def test_delimiter_two(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold block", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,correct)
    
    def test_delimiter_three(self):
        node = TextNode("**This is text with a bold block word**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct = [
        TextNode("**This is text with a bold block word**", TextType.BOLD)
        ]
        self.assertEqual(new_nodes,correct)
    
    def test_delimiter_four(self):
        node = TextNode("**This is text with a bold block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    
    def test_multiple_text_nodes(self):
        nodes = [
            TextNode("Boots is **great** and ", TextType.TEXT),
            TextNode("very **helpful** indeed", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        correct = [
            TextNode("Boots is ", TextType.TEXT),
            TextNode("great", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("very ", TextType.TEXT),
            TextNode("helpful", TextType.BOLD),
            TextNode(" indeed", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, correct)
    
    def test_mixed_types_unchanged_non_text(self):
        nodes = [
            TextNode("This is **bold** text", TextType.TEXT),
            TextNode("Already bold", TextType.BOLD),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        correct = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("Already bold", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, correct)
    
    def test_no_delimiters_in_text(self):
        node = TextNode("Just plain text, nothing special", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct = [TextNode("Just plain text, nothing special", TextType.TEXT)]
        self.assertEqual(new_nodes, correct)
    
    def test_multiple_pairs_in_one_node(self):
        node = TextNode("This has **two** bold **sections** here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct = [
            TextNode("This has ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" bold ", TextType.TEXT),
            TextNode("sections", TextType.BOLD),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, correct)
    
    def test_italic_underscore_delimiter(self):
        node = TextNode("Some _italic_ and _more_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        correct = [
            TextNode("Some ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("more", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, correct)
    
    def test_unbalanced_in_middle_node(self):
        nodes = [
            TextNode("Start **ok** ", TextType.TEXT),
            TextNode("then **bad", TextType.TEXT),
        ]
        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

