import unittest

from block_level_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node
)
from htmlnode import HTMLNode

class TestBlockLevelMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ["# This is a heading",
                                  "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                                  """* This is the first list item in a list block
* This is a list item
* This is another list item"""])

    def test_block_to_block_type_heading(self):
        block = "###### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")

    def test_block_to_block_type_code(self):
        block = "```\n This is a code block \n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "code")

    def test_block_to_block_type_quote(self):
        block = "> This is a quote block\n> Line 2 of quote block\n> Line 3 of quote block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "quote")

    def test_block_to_block_type_unordered_list(self):
        block = "* This is an unordered list block\n* Line 2 of unordered list block\n* Line 3 of unordered list block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "unordered list")

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is an ordered list block\n2. Line 2 of ordered list block\n3. Line 3 of ordered list block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "ordered list")

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")


    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()
