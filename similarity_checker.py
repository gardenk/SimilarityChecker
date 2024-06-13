class SimilarityCheck:
    def check(self, A, B):
        if not len(A) or not len(B):
            raise TypeError
