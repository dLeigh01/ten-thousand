from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(roll):
        score = 0
        sort = Counter(roll).most_common()

        if sorted(roll) == [1, 2, 3, 4, 5, 6]:
            return 1500

        if len(sort) == 3:
            if sort[0][1] == 2:
                return 1500

        if len(sort) == 2:
            if sort[0][1] == 3 & sort[1][1] == 3:
                return 1200

        for item in sort:
            if item[0] == 1:
                if item[1] < 3:
                    score += 100 * item[1]
                else:
                    score += 1000 * (item[1] - 2)
            elif item[0] == 5:
                if item[1] < 3:
                    score += 50 * item[1]
                else:
                    score += (5 * 100) + ((5 * 100) * (item[1] - 3))
            elif item[1] >= 3:
                score += (item[0] * 100) + ((item[0] * 100) * (item[1] - 3))
                
        return score

    @staticmethod
    def roll_dice(num):
        result = []
        i = 0
        while i < num:
            roll = random.randint(1, 6)
            result.append(roll)
            i += 1
        return tuple(result)

if __name__ == '__main__':
    game = GameLogic()
    game.calculate_score(game.roll_dice(6))