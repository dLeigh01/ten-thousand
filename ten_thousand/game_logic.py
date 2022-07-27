from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(roll):
        score = 0
        sort = Counter(roll).most_common()

        # straight
        if sorted(roll) == [1, 2, 3, 4, 5, 6]:
            return 1500

        # 3 pairs
        if len(sort) == 3:
            if sort[0][1] == 2:
                return 1500

        for item in sort:
            # Ones
            if item[0] == 1:
                if item[1] < 3:
                    score += 100 * item[1]
                else:
                    score += 1000 * (item[1] - 2)
            # Fives
            elif item[0] == 5:
                if item[1] < 3:
                    score += 50 * item[1]
                else:
                    score += (5 * 100) + ((5 * 100) * (item[1] - 3))
            # 3 or more of any other number
            elif item[1] >= 3:
                score += (item[0] * 100) + ((item[0] * 100) * (item[1] - 3))

        return score

    @staticmethod
    def roll_dice(num):
        result = []
        i = 0
        # roll until the number of dice rolled is the amount passed in
        while i < num:
            roll = random.randint(1, 6)
            result.append(roll)
            i += 1
        return tuple(result)

    @staticmethod
    def get_scorers(dice):
        scorers = [die for die in dice if die == 1 or die == 5]
        return tuple(scorers)

    @staticmethod
    def validate_keepers(roll, keepers):
        validation = GameLogic.get_scorers(roll)
        if tuple(reversed(sorted(validation))) == keepers:
            return True
        return False

# rolls for each sim
bank_first_for_two_rounds_rolls = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4), (6, 6, 5, 4, 2, 1)]
bank_one_roll_then_quit_rolls = [(4, 2, 6, 4, 6, 5), (6, 4, 5, 2, 3, 1)]
one_and_done_rolls = [(4, 4, 5, 2, 3, 1)]
cheat_and_fix_rolls = [(5, 2, 3, 5, 4, 2), (5, 2, 3, 5, 4, 2)]
hot_dice_rolls = [(2, 3, 1, 3, 1, 2), (4, 1, 4, 4, 3, 4), (3, 2, 3, 2, 1, 4)]
repeat_roller_rolls = [(2, 3, 1, 3, 4, 2), (4, 2, 4, 4, 6), (3, 2, 3, 2, 1, 4)]
zilcher_rolls = [(1, 2, 5, 1, 2, 1), (4, 4), (1, 1, 2, 5, 1, 6)]

rolls = hot_dice_rolls
# changeable rolls for testing purposes
class TestLogic(GameLogic):
    @staticmethod
    def roll_dice(num):
        if len(rolls):
            result = rolls.pop(0)
            return result

        return GameLogic.roll_dice(num)
