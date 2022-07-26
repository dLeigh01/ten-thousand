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

# changeable rolls for testing purposes
class TestLogic:
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
        result = (4, 4, 5, 2, 3, 1)
        return result

# change tuple to list of string values
def tuple_to_list(tup):
    li = []
    for item in tup:
        li.append(str(item))
    return li

################################################################################
################################## RUN GAME ####################################
################################################################################

def play_game(logic):
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")

    if choice == "n":
        print("OK. Maybe another time")
        return
    elif choice == "y":
        count = 1

        # only run game for 20 rounds
        while count <= 20:
            print(f"Starting round {count}")
            print("Rolling 6 dice...")
            roll = tuple_to_list(logic.roll_dice(6))
            print(f"*** {' '.join(roll)} ***")
            print("Enter dice to keep, or (q)uit:")
            choice = input("> ")

            if choice == "q":
                print("Thanks for playing. You earned 0 points")
                return
            # increase count after each round
            count += 1


if __name__ == '__main__':
    play_game(TestLogic())