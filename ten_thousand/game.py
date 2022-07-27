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

        if round_result == 'q':
            quit_game(total_score)
            return

        total_score = round_result
        round_count += 1
    return


def rounds(Logic, round_count, total_score):
    dice = 6
    round_score = 0
    choice = round_start(Logic, round_count, dice, total_score, round_score)

    # quit game
    if choice == "q":
        return choice

    while True:
        held_dice = format_dice_choice(choice)
        round_score += calculate_score(Logic, held_dice)
        dice -= len(held_dice)
        choice = roll_or_bank(round_score, dice)

        # quit game
        if choice == "q":
            return choice

        # roll again
        if choice == "r":
            zilch = roll_dice(Logic, dice, total_score, round_score, round_count)
            if zilch == 0:
                return zilch
            continue

        # bank total, start next round
        if choice == "b":
            return bank_points(total_score, round_score, round_count)


def round_start(Logic, round_count, dice, total_score, round_score):
    print(f"Starting round {round_count}")
    print(f"Rolling {dice} dice...")
    zilch = roll_dice(Logic, dice, total_score, round_score, round_count)
    if zilch == 0:
        return zilch
    print("Enter dice to keep, or (q)uit:")
    return input("> ")


def roll_or_bank(round_score, dice):
    print(f"You have {round_score} unbanked points and {dice} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    return input("> ")


def calculate_score(Logic, held_dice):
    this_roll = Logic.calculate_score(held_dice)
    return this_roll


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
def format_dice_choice(text):
    return tuple([int(num) for num in text if num.isdigit()])


def roll_dice(Logic, dice, total_score, round_score, round_count):
    roll = format_roll(Logic.roll_dice(dice))
    print(f"*** {roll} ***")
    zilch = zilch_check(Logic, roll, total_score, round_score, round_count)
    if zilch == 0:
        return zilch
    return

def zilch_check(Logic, roll, total_score, round_score, round_count):
    score = calculate_score(Logic, format_dice_choice(roll))
    if score == 0:
        return zilcher(total_score, round_count)
    return

def zilcher(total_score, round_count):
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")
    bank_points(total_score, 0, round_count)
    return 0


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
    run_game(GameLogic)
