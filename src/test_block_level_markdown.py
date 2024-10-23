import unittest

from block_level_markdown import (
    markdown_to_blocks,
    block_to_block_type
)


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


if __name__ == "__main__":
    unittest.main()
