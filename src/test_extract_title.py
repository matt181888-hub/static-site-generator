import unittest
from extract_title import *

class TestExtractTitle(unittest.TestCase):
    def test_one(self):
        md = """# Hello       
## this isnt a header
"""     
        test = extract_title(md)
        correct = "Hello"
        self.assertEqual(
            test,
            correct
        )
    
    def test_two_longer(self):
        md ="""

![JRR Tolkien sitting](/images/tolkien.png)
# Tolkien Fan Club
Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

## Reasons I like Tolkien

- You can spend years studying the legendarium and still not understand its depths
- It can be enjoyed by children and adults alike
- Disney _didn't ruin it_ (okay, but Amazon might have)
- It created an entirely new genre of fantasy

## My favorite characters (in order)
"""
        test = extract_title(md)
        correct = "Tolkien Fan Club"
        self.assertEqual(
            test,
            correct
        )
