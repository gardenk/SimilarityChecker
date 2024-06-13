class SimilarityCheck:
    def __init__(self):
        self.MAX_LENGTH_SCORE = 60
    def check(self, A, B):
        if not len(A) or not len(B):
            raise TypeError

        if len(A) == len(B):
            return self.MAX_LENGTH_SCORE

        elif len(A) > len(B):
            return 60 - 60*(len(A) - len(B))/len(B)
