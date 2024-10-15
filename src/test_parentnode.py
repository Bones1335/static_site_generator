import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_values(self):
        node = ParentNode("p",
                          [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")]
                          )
        self.assertEqual(node.tag, "p")

    def test_to_html(self):
        node = ParentNode("p",
                          [
                           LeafNode("b", "Bold text"),
                           LeafNode(None, "Normal text"),
                           LeafNode("i", "italic text"),
                           LeafNode(None, "Normal text"),
                          ],
                          )
        self.assertEqual(node.to_html(),
                         '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
                         )

    def test_repr(self):
        node = ParentNode("p",
                          [
                           LeafNode("b", "Bold text"),
                           LeafNode(None, "Normal text"),
                           LeafNode("i", "italic text"),
                           LeafNode(None, "Normal text"),
                          ],
                          )
        self.assertEqual(node.__repr__(),
                         'ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)'
                         )


if __name__ == "__main__":
    unittest.main()
