class SimilarityCheck:
    def check(self, A, B):
        length_score = 0
        alpha_score = self.check_alphabet(A, B)
        return length_score + alpha_score

    def check_alphabet(self, A, B):
        if not len(A) or not len(B):
            raise TypeError
