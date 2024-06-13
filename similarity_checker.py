class SimilarityCheck:
    def __init__(self):
        self.MAX_ALPHA_SCORE = 40
    def check(self, A, B):
        length_score = 0
        alpha_score = self.check_alphabet(A, B)
        return length_score + alpha_score

    def check_alphabet(self, A, B):
        if not len(A) or not len(B):
            raise TypeError
        A, B = A.lower(), B.lower()
        A_set = set(A)
        B_set = set(B)
        if not len(A_set - B_set) and not len(B_set - A_set):
            return self.MAX_ALPHA_SCORE