import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode('Matthew', TextType.ITALIC)
        node2 = TextNode('Matthew', TextType.ITALIC, url='http://google.com')
        self.assertNotEqual(node, node2)

    def test_capitalization(self):
        node = TextNode('matthew', TextType.TEXT)
        node2 = TextNode('Matthew', TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_font(self):
        node = TextNode('matthew', TextType.TEXT)
        node2 = TextNode('matthew', TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_URL(self):
        node = TextNode('matthew', TextType.CODE, url='http://googl.com')
        node2 = TextNode('matthew', TextType.CODE, url='http://google.com')
        self.assertNotEqual(node, node2)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "http://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "http://google.com"})

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "http://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src" : "http://google.com",
                                           "alt" : "This is a text node"})
if __name__ == "__main__":
    unittest.main()