from unittest import TestCase

from similarity_checker import SimilarityCheck


class TestSimilarityCheck(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = SimilarityCheck()

    def test_none_strings(self):
        try:
            self.checker.check("", "")
        except TypeError:
            pass

    def test_same_length_strings(self):
        self.assertEqual(self.checker.check("abc", "def"), 60)

    def test_A_longer_than_B(self):
        self.assertEqual(self.checker.check("abcde", "def"), 20)
