class SimilarityCheck:
    def __init__(self):
        self.MAX_LENGTH_SCORE = 60
    def check(self, A, B):
        if not len(A) or not len(B):
            raise TypeError

        if len(A) >= len(B):
            return self.calc_length_score(len(A), len(B))
        else:
            return self.calc_length_score(len(B), len(A))

    def calc_length_score(self, A_len, B_len):
        return max(60 - 60 * (A_len - B_len) / B_len, 0)