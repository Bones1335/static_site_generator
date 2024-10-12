import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("a", "This is an HTML node", [HTMLNode("p")], {"href": "google.com"})
        props = node.props_to_html()
        self.assertEqual(' href="google.com"', props)

    def test_props2(self):
        node = HTMLNode("a", "This is an HTML node", [HTMLNode("p")], {"href": "google.com", "target": "_blank"})
        props = node.props_to_html()
        self.assertEqual(' href="google.com" target="_blank"', props)

    def test_repr(self):
        node = HTMLNode("a", "This is an HTML node", [], {"href": "google.com"})
        self.assertEqual(
            "HTMLNode(a, This is an HTML node, [], {'href': 'google.com'})",
            repr(node)
        )


if __name__ == "__main__":
    unittest.main()
