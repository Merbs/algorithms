###
# Pots of Gold
# Given an array of numbers (pots of gold in a line), two players alternate
# turns choosing from one of the two ends. Whoever gets the larger sum wins.
# Design an algorithm that plays optimally with the smallest time complexity.
###

# This is a dynamic programming problem because it has 'optimal substructure'.
# That is, given an array [a, b, c, d, e], we'll need to solve the subarrays
# [a, b, c, d] and [b, c, d] and [c, d]. If we approach this problem naively,
# it will take a lot of time because we'll be solving [c, d] many times.
# Instead, what we're going to do is cache it, and trade space for time.
class PotsOfGoldGame:
    def __init__(self, gold):
        self.cache= {} # key is tuple (start_index, end_index), value is score
        self.gold = gold
        self.size = len(gold)

        self.computeOptimalPlays()

    def score(self, left, right):
        return self.cache[(left, right)]['score']

    def choose(self, left, right):
        return self.cache[(left, right)]['choice']

    def computeOptimalPlays(self):
        """Creates our cache with optimal plays for all subgames"""

        # Base Cases
        for i in range(self.size):
            # If there is only one pot of gold left, take that pot
            self.cache[(i, i)] = {'score': self.gold[i], 'choice': 'left'}
        for i in range(self.size - 1):
            # If there are two pots of gold left, take the larger one
            self.cache[(i, i+1)] = {
                'score': max(self.gold[i], self.gold[i+1]),
                'choice': 'left' if self.gold[i] >= self.gold[i+1] else 'right'
            }

        # Inductive Step
        for length in range(2,self.size):
            for j in range(self.size - length):
                k = j + length
                # Here, we decide whether to take from the left (the j side)
                # or the right (the k side). If we take from the left, then
                # (if) our opponent makes the optimal move, we'll be left with
                # the minimum of two pots taken from the left or one pot taken
                # from either side (because it is a zero-sum game).
                # Similarly, if we take from the right, then our worst-case
                # score is the minimum of the subgame situation where either
                # two pots are taken from the right or one from either side.
                # The subgame structure is what makes this a DP problem.
                leftMove = self.gold[j]
                rightMove = self.gold[k]
                afterLeftMove = min(self.score(j+2,k), self.score(j+1,k-1))
                afterRightMove = min(self.score(j+1,k-1), self.score(j,k-2))

                if leftMove + afterLeftMove >= rightMove + afterRightMove:
                    score = leftMove + afterLeftMove
                    choice = 'left'
                else:
                    score = rightMove + afterRightMove
                    choice = 'right'

                self.cache[(j,k)] = {
                    'score': score,
                    'choice': choice
                }

    def getOptimalPlay(self):
        left, right = 0, self.size-1
        play = []
        while left <= right:
            if self.choose(left,right) == 'left':
                option = left
                left, right = [left+1, right]
            else:
                option = right
                left, right = [left, right-1]
            play.append(option)
        return play

    def getOptimalScores(self):
        if self.size == 0: return 0, 0
        if self.size == 1: return self.gold[0], 0

        left, right = 0, self.size-1
        scoreA = self.score(left, right)
        if self.choose(left,right) == 'left':
            scoreB = self.score(left+1, right)
        else:
            scoreB = self.score(left, right-1)
        return scoreA, scoreB


# In our test cases, the first element of the set is our "pots of gold",
# whereas the second is the player scores (first-mover and second-mover).
# We might also look at the array of the indices of the pots of gold taken.
# However, there may be multiple paths to the same score.
test_cases = [
    ([3], (3, 0)),
    ([3, 4], (4, 3)),
    ([3, 4, 5], (8, 4)),
    ([9, 7, 5, 3, 1, 0, 2, 4, 6, 8], (25, 20)),
    ([1, 3, 4, 12, 5, 7], (22, 10)),
]

for gold, ans in test_cases:
    game = PotsOfGoldGame(gold)
    assert game.getOptimalScores() == ans
