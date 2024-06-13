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

    def test_same_alpha_strings(self):
        self.assertEqual(self.checker.check("ASD", "DSA"), 40)
        self.assertEqual(self.checker.check("ASD", "asd"), 40)
        self.assertEqual(self.checker.check("AAABB", "BABA"), 40)

    def test_all_different_strings(self):
        self.assertEqual(self.checker.check("A", "BB"), 0)