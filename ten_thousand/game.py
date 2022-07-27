from ten_thousand.game_logic import GameLogic, TestLogic

# welcome player and ask if they want to play
def welcome_message():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    return input("> ")

def decline_game():
    print("OK. Maybe another time")
    return

def accept_game(logic):
    round_count = 1
    max_rounds = 20
    total_score = 0

    while round_count <= max_rounds:
        # TODO rounds()
        dice = 6
        round_score = 0
        print(f"Starting round {round_count}")
        print(f"Rolling {dice} dice...")
        choice = roll_dice(logic, dice)

        if choice == "q":
            quit_game(total_score)
            return

        while True:
            # calculate score
            held_dice = string_to_tuple(choice)
            this_roll = logic.calculate_score(held_dice)
            round_score += this_roll
            dice -= len(held_dice)
            print(f"You have {round_score} unbanked points and {dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            choice = input("> ")

            # quit game
            if choice == "q":
                quit_game(total_score)
                return

            # roll again
            if choice == "r":
                choice = roll_dice(logic, dice)

                # quit game
                if choice == "q":
                    quit_game(total_score)
                    return
                continue

            # bank total, start next round
            if choice == "b":
                total_score = bank_points(total_score, round_score, round_count)
                break

        round_count += 1
    return

def rounds():
    pass

def quit_game(score):
    print(f"Thanks for playing. You earned {score} points")
    return

def bank_points(total_score, round_score, round_count):
    total_score += round_score
    print(f"You banked {round_score} points in round {round_count}")
    print(f"Total score is {total_score} points")
    return total_score

################################################################################
############################ HELPER FUNCTIONS ##################################
################################################################################

# change tuple from roll_dice to list of string values
def format_roll(tup):
    text = [str(item) for item in tup]
    return ' '.join(text)

# change string of numbers to tuple of integers
def string_to_tuple(text):
    return tuple([int(num) for num in text if num.isdigit()])

# roll dice and ask for keep or quit
def roll_dice(logic, dice):
    roll = format_roll(logic.roll_dice(dice))
    print(f"*** {roll} ***")
    print("Enter dice to keep, or (q)uit:")
    return input("> ")

################################################################################
################################## RUN GAME ####################################
################################################################################

def run_game(logic):
    choice = welcome_message()

    if choice == "n":
        decline_game()
    elif choice == "y":
        accept_game(logic)


if __name__ == '__main__':
    run_game(GameLogic())