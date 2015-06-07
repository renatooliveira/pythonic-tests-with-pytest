import unittest


def to_upper(text):
    return text.upper()


class TestToUpper(unittest.TestCase):

    def test_to_upper(self):
        self.assertEqual(to_upper("pug"), "PuG")
