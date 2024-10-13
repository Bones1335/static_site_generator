import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_values(self):
        node = LeafNode("a", "This is a Leaf node", {"href": "google.com", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "This is a Leaf node")
        self.assertEqual(node.props, {"href": "google.com", "target": "_blank"})

    def test_to_html(self):
        node = LeafNode("a", "This is a Leaf node", {"href": "google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="google.com" target="_blank">This is a Leaf node</a>')

    def test_repr(self):
        node = LeafNode("a", "This is a Leaf node", {"href": "google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), "LeafNode(a, This is a Leaf node, {'href': 'google.com', 'target': '_blank'})")


if __name__ == "__main__":
    unittest.main()
