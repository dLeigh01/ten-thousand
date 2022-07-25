from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(roll):
        score = 0
        sort = Counter(roll).most_common

        return score

    @staticmethod
    def roll_dice(int):
        result = []
        i = 0
        while i < int:
            result.append(1)
            i += 1
        return tuple(result)