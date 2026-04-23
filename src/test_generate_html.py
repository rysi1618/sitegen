import unittest
from generate_html import *

class TestGenerateHTML(unittest.TestCase):
    # print(extract_title("# Header blah"))
    # print(extract_title("testing\n# Second line\nThird line"))
    # print(extract_title("There is no title\nNor here\n"))

    def test_extract_title_first_line(self):
        title = extract_title("# Header first line")
        self.assertEqual(title, "Header first line")

    def test_extract_title_second_line(self):
        title = extract_title("testing\n# Second line\nThird line")
        self.assertEqual(title, "Second line")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass

    # def test_extract_title_no_title(self):
    #     title = extract_title("There is no title\nNor here\n")
    #     self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()