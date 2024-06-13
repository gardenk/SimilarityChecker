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
        result = self.checker.check("abc", "def")
        self.assertEqual(result, 60)