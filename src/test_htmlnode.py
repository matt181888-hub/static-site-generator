import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode(tag = "a", 
                        value = "why the leafs suck", 
                        props ={"href": "https://www.google.com",
                                "target": "_blank"} 
        )
        result = node.props_to_html()
        correct =' href="https://www.google.com" target="_blank"'
        self.assertEqual(result,correct)
    
    def test_prop_two(self):
        node = HTMLNode(tag = "img",
                        value = "Karens",
                        props ={"src": "https://example.com/image.png",
                                "alt": "A descriptive caption",
                                "width": "300",
                                "height": "200"}, 
        )
        result = node.props_to_html()
        correct =' src="https://example.com/image.png" alt="A descriptive caption" width="300" height="200"'
        self.assertEqual(result,correct)
    
    def test_prop_input(self):
        node = HTMLNode(
            tag="input",
            value="",
            props={"type": "text", "placeholder": "Enter your name", "value": "Mathias"}
        )
        result = node.props_to_html()
        correct = ' type="text" placeholder="Enter your name" value="Mathias"'
        self.assertEqual(result, correct)
    
    def test_prop_button(self):
        node = HTMLNode(
            tag="button",
            value="Submit",
            props={"type": "submit", "disabled": "true"}
        )
        result = node.props_to_html()
        correct = ' type="submit" disabled="true"'
        self.assertEqual(result, correct)
    
    def test_prop_paragraph(self):
        node = HTMLNode(
            tag="p",
            value="Hello world",
            props={"class": "intro-text", "id": "main-paragraph"}
        )
        result = node.props_to_html()
        correct = ' class="intro-text" id="main-paragraph"'
        self.assertEqual(result, correct)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "Hello, world!")
        self.assertEqual(node.to_html(), "<img>Hello, world!</img>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_valueError(self):
        node = LeafNode(tag='a', value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_value_error(self):
        node = LeafNode( tag = None, value = "Hello, world!")
        self.assertEqual(node.to_html(), f"{node.value}")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_grandchildren(self):
        greatgrandchild_node = LeafNode("a", "great")
        grandchild_node = LeafNode("b", "children")
        child_node = ParentNode("p", [grandchild_node, greatgrandchild_node])
        parent_node = ParentNode("span", [child_node])
        grandparent_node = ParentNode("div", [parent_node])
        self.assertEqual(
            grandparent_node.to_html(),
            "<div><span><p><b>children</b><a>great</a></p></span></div>",
        )
    
    def test_no_tag_parent(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "x")]).to_html()
    
    def test_tag_untagged(self):
        node = ParentNode("p", [
            LeafNode("b", "bold"),
            LeafNode(None, " and "),
            LeafNode("i", "italic"),
        ])
        self.assertEqual(node.to_html(), "<p><b>bold</b> and <i>italic</i></p>")
    
    def test_props_parent(self):
        node = ParentNode("div", [LeafNode(None, "x")], {"class": "box"})
        self.assertEqual(node.to_html(), '<div class="box">x</div>')
    
    def test_props_parent_child(self):
        child = LeafNode("span", "ok", {"id": "child"})
        parent = ParentNode("div", [child], {"class": "outer"})
        self.assertEqual(
            parent.to_html(),
            '<div class="outer"><span id="child">ok</span></div>',
        )


