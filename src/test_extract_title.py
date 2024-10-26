import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is the header"
        title = extract_title(markdown)
        self.assertEqual(title, "This is the header")


if __name__ == "__main__":
    unittest.main()
