import unittest

from block_level_markdown import (
    markdown_to_blocks
)


class TestBlockLevelMarkdown(unittest.TestCase):
    def test_code_delimiter(self):
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

            
if __name__ == "__main__":
    unittest.main()
