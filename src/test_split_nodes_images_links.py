import unittest
from textnode import *
from htmlnode import *
from split_nodes_delimiter import *
from split_nodes_images_links import *

class TestSplitNodesImagesLinks(unittest.TestCase):
    def test_one(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual([
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
                new_nodes)
        
    def test_two(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node_two = TextNode("There is no link here", TextType.TEXT)
        new_nodes = split_nodes_links([node,node_two])
        self.assertEqual([
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode("There is no link here", TextType.TEXT)
            ],
                new_nodes)
        
    def test_three_LinkAtBeginning(self):
        node = TextNode(
            "[start](https://example.com) of the sentence",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual([
            TextNode("start", TextType.LINK, "https://example.com"),
            TextNode(" of the sentence", TextType.TEXT),
        ], new_nodes)
    
    def test_four_LinkAtTheEnd(self):
        node = TextNode(
            "Click this [end](https://example.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual([
            TextNode("Click this ", TextType.TEXT),
            TextNode("end", TextType.LINK, "https://example.com"),
        ], new_nodes)
    
    def test_five_AdjacentLinks(self):
        node = TextNode(
            "[one](https://a.com)[two](https://b.com)[three](https://c.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual([
            TextNode("one", TextType.LINK, "https://a.com"),
            TextNode("two", TextType.LINK, "https://b.com"),
            TextNode("three", TextType.LINK, "https://c.com"),
        ], new_nodes)

    def test_six_BracketsButNoLink(self):
        node = TextNode(
            "Not a link: [just brackets] and (just parentheses)",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual([
            TextNode("Not a link: [just brackets] and (just parentheses)", TextType.TEXT),
        ], new_nodes)
    
    def test_seven_AlreadyLinkNode(self):
        node1 = TextNode(
            "before [link](https://x.com) after",
            TextType.TEXT
        )
        node2 = TextNode("already a link", TextType.LINK, "https://z.com")

        new_nodes = split_nodes_links([node1, node2])

        self.assertEqual([
            TextNode("before ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://x.com"),
            TextNode(" after", TextType.TEXT),
            TextNode("already a link", TextType.LINK, "https://z.com"),
        ], new_nodes)

    def test_eight_RepeatedLink(self):
        node = TextNode(
            "Here is [x](https://same.com) and again [x](https://same.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual([
            TextNode("Here is ", TextType.TEXT),
            TextNode("x", TextType.LINK, "https://same.com"),
            TextNode(" and again ", TextType.TEXT),
            TextNode("x", TextType.LINK, "https://same.com"),
        ], new_nodes)

    def test_nine_LinkTextPunctuation(self):
        node = TextNode(
            "Check this [hello world!](https://example.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual([
            TextNode("Check this ", TextType.TEXT),
            TextNode("hello world!", TextType.LINK, "https://example.com"),
        ], new_nodes)

    def test_split_images_one(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_two_ImageAtStart(self):
        node = TextNode(
            "![start](https://img.com/start.png) begins the sentence",
            TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("start", TextType.IMAGE, "https://img.com/start.png"),
            TextNode(" begins the sentence", TextType.TEXT),
        ], new_nodes)
    
    def test_split_images_three_ImageAtEnd(self):
        node = TextNode(
            "This ends with an image ![end](https://img.com/end.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("This ends with an image ", TextType.TEXT),
            TextNode("end", TextType.IMAGE, "https://img.com/end.png"),
        ], new_nodes)
    
    def test_split_images_four_AdjacentImages(self):
        node = TextNode(
            "![one](https://a.com/1.png)![two](https://a.com/2.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("one", TextType.IMAGE, "https://a.com/1.png"),
            TextNode("two", TextType.IMAGE, "https://a.com/2.png"),
        ], new_nodes)

    def test_split_images_five_NoImages(self):
        node = TextNode("There are no images here", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("There are no images here", TextType.TEXT),
        ], new_nodes)
    
    def test_split_images_six_ImageMixedWithText(self):
        node = TextNode(
            "Before![pic](https://ex.com/p.png)After",
            TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("Before", TextType.TEXT),
            TextNode("pic", TextType.IMAGE, "https://ex.com/p.png"),
            TextNode("After", TextType.TEXT),
        ], new_nodes)

    def test_split_images_seven_MultipleNodesSomeImages(self):
        node1 = TextNode("first ![one](https://img.com/1.png)", TextType.TEXT)
        node2 = TextNode("nothing here", TextType.TEXT)
        node3 = TextNode("![two](https://img.com/2.png) end", TextType.TEXT)

        new_nodes = split_nodes_images([node1, node2, node3])
        self.assertEqual([
            TextNode("first ", TextType.TEXT),
            TextNode("one", TextType.IMAGE, "https://img.com/1.png"),
            TextNode("nothing here", TextType.TEXT),
            TextNode("two", TextType.IMAGE, "https://img.com/2.png"),
            TextNode(" end", TextType.TEXT),
        ], new_nodes)
    
    def test_split_images_eight_RepeatedSameImage(self):
        node = TextNode(
            "![x](https://img.com/x.png) and again ![x](https://img.com/x.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("x", TextType.IMAGE, "https://img.com/x.png"),
            TextNode(" and again ", TextType.TEXT),
            TextNode("x", TextType.IMAGE, "https://img.com/x.png"),
        ], new_nodes)
    
    def test_split_images_nine_ImageWithSpacesInAltText(self):
        node = TextNode(
            "This is ![hello world pic](https://img.com/hello.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("hello world pic", TextType.IMAGE, "https://img.com/hello.png"),
        ], new_nodes)
    
    def test_split_images_ten_ImageNextToPunctuation(self):
        node = TextNode(
            "Look![img](https://img.com/i.png), right here!",
            TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertEqual([
            TextNode("Look", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://img.com/i.png"),
            TextNode(", right here!", TextType.TEXT),
        ], new_nodes)








    




