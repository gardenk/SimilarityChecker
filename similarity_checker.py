class SimilarityCheck:
    def __init__(self):
        self.MAX_LENGTH_SCORE = 60

    def check(self, A, B):
        length_score = self.check_length(A, B)
        return length_score

    def check_length(self, A, B):
        if not len(A) or not len(B):
            raise TypeError

        if len(A) >= len(B):
            return self.calc_length_score(len(A), len(B))
        else:
            return self.calc_length_score(len(B), len(A))

    def calc_length_score(self, A_len, B_len):
        return max(self.MAX_LENGTH_SCORE - self.MAX_LENGTH_SCORE * (A_len - B_len) / B_len, 0)