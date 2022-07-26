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
        result = (4, 2, 6, 4, 6, 5)
        return result

# change tuple to list of string values
def tuple_to_list(tup):
    li = []
    for item in tup:
        li.append(str(item))
    return li

# change string of numbers to tuple of integers
def string_to_tuple(text):
    li = list(text)
    int_li = []
    for item in li:
        int_li.append(int(item))

    return tuple(int_li)

# quit game and print score
def quit_game(score):
    print(f"Thanks for playing. You earned {score} points")
    return

# roll dice and ask for keep or quit
def roll_to_choice(logic, dice):
    roll = tuple_to_list(logic.roll_dice(dice))
    print(f"*** {' '.join(roll)} ***")
    print("Enter dice to keep, or (q)uit:")
    return input("> ")

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
        total_score = 0

        # only run game for 20 rounds
        while count <= 20:
            dice = 6
            round_score = 0
            print(f"Starting round {count}")
            print(f"Rolling {dice} dice...")
            choice = roll_to_choice(logic, dice)

            if choice == "q":
                quit_game(total_score)
                return

            while True:
                # calculate score
                this_roll = logic.calculate_score(string_to_tuple(choice))
                round_score += this_roll
                dice -= len(list(choice))
                print(f"You have {round_score} unbanked points and {dice} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                choice = input("> ")

                # quit game
                if choice == "q":
                    quit_game(total_score + round_score)
                    return

                # roll again
                if choice == "r":
                    choice = roll_to_choice(logic, dice)

                    # quit game
                    if choice == "q":
                        quit_game(total_score + round_score)
                        return
                    continue

                # bank total, start next round
                if choice == "b":
                    total_score += round_score
                    print(f"You banked {round_score} points in round {count}")
                    print(f"Total score is {total_score} points")
                    break

            # increase count after each round
            count += 1


if __name__ == '__main__':
    play_game(GameLogic())