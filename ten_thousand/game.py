from ten_thousand.game_logic import GameLogic, TestLogic

# welcome player and ask if they want to play
def welcome_message():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    return input("> ")


def decline_game():
    print("OK. Maybe another time")
    return


def accept_game(Logic):
    round_count = 1
    max_rounds = 20
    total_score = 0

    while round_count <= max_rounds:
        round_result = rounds(Logic, round_count, total_score)

        if round_result == -1:
            quit_game(total_score)
            return

        total_score = round_result
        round_count += 1
    return


def rounds(Logic, round_count, total_score):
    dice = 6
    round_score = 0
    print(f"Starting round {round_count}")

    while True:
        roll = roll_dice(Logic, dice)
        # check if the roll scored
        if zilcher(Logic, roll) == 0:
            bank_points(total_score, 0, round_count)
            return 0
        while True:
            choice = keep_or_quit()
            # quit game
            if choice == "q":
                return -1
            held_dice = format_dice(choice)
            if Logic.validate_keepers(format_dice(roll), held_dice) is False: #TODO ADD THIS WHOLE SECTION AND 44-49 TO A FUNCTION
                cheater(roll)
                continue
            break

        round_score += Logic.calculate_score(held_dice)
        dice -= len(held_dice)
        if dice == 0:
            dice = 6
        choice = roll_or_bank(round_score, dice)

        # quit game
        if choice == "q":
            return -1

        # bank total, start next round
        if choice == "b":
            return bank_points(total_score, round_score, round_count)


def keep_or_quit():
    print("Enter dice to keep, or (q)uit:")
    return input("> ")


def roll_or_bank(round_score, dice):
    print(f"You have {round_score} unbanked points and {dice} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    return input("> ")


def quit_game(score):
    print(f"Thanks for playing. You earned {score} points")
    return


def bank_points(total_score, round_score, round_count):
    total_score += round_score
    print(f"You banked {round_score} points in round {round_count}")
    print(f"Total score is {total_score} points")
    return total_score


# change tuple from roll_dice to list of string values
def format_roll(tup):
    text = [str(item) for item in tup]
    return ' '.join(text)


# change string of numbers to tuple of integers
def format_dice(text):
    return tuple([int(num) for num in text if num.isdigit()])


def roll_dice(Logic, dice):
    print(f"Rolling {dice} dice...")
    roll = format_roll(Logic.roll_dice(dice))
    print(f"*** {roll} ***")
    return roll


def zilcher(Logic, roll):
    if Logic.calculate_score(format_dice(roll)) == 0:
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        return 0
    return


def cheater(roll):
    print("Cheater!!! Or possibly made a typo...")
    print(f"*** {roll} ***")


################################################################################
################################## RUN GAME ####################################
################################################################################

def run_game(Logic):
    choice = welcome_message()

    if choice == "n":
        decline_game()
    elif choice == "y":
        accept_game(Logic)

if __name__ == '__main__':
    run_game(TestLogic)
