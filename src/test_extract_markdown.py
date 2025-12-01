import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_markdown_images_multiple(self):
        text = (
            "![one](url1.png) some text "
            "![two](url2.jpg) more text "
            "![three](url3.gif)"
        )
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("one", "url1.png"),
                ("two", "url2.jpg"),
                ("three", "url3.gif"),
            ],
            matches
        )

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("There are no images here.")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_ignores_links(self):
        text = "[link](https://example.com) but no images"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "This has a [link](https://example.com/page)"
        )
        self.assertListEqual(
            [("link", "https://example.com/page")],
            matches
        )

    def test_extract_markdown_links_multiple(self):
        text = (
            "[google](https://google.com) and "
            "[github](https://github.com) are links"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("google", "https://google.com"),
                ("github", "https://github.com"),
            ],
            matches
        )

    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links("No links here!")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_ignores_images(self):
        text = (
            "![alt text](https://i.imgur.com/x.png) "
            "and [link](https://example.com)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("link", "https://example.com")],
            matches
        )


