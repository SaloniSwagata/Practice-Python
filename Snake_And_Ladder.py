#Snake and Ladder Game
import random

snakes = {
    17:7,54:34,62:19,98:79}
ladders = {
    3:38,24:33,42:93,72:84}
max_value = 100
dice_face = 6
    
def welcome_message():
    print("###### Welcocme to Snakes & Ladders Game ######")

def get_players_name():
    player1_name = input("Enter the name of Player1: ")
    player2_name = input("Enter the name of Player2: ")

def get_dice_value():
    dice_value= random.randint(1,dice_face)
    return dice_value


def snake_ladder(current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value == max_value:
        return current_value

    if current_value > max_value:
        print(" Your final position is "+old_value)
        return old_value

    if current_value in snakes:
        final_value = snakes.get(current_value)

    elif current_value in ladders:
        final_value = ladders.get(current_value)

    else:
        final_value = current_value
    print(" Your final position is {}".format(final_value))

    return final_value


def check_win(player_name, position):
    if max_value == position:
        print(player_name + " won the game")
        print("###### Game Succesfully Finished ######")
        return 1
    else:
        return 0
        


def start():
    welcome_message()
    get_players_name()

    player1_current_position = 0
    player2_current_position = 0
    print("###### Let us Start ######")
    while True:
        quits = 0
        while True:
            input_1 = input("Player 1: ")
            if input_1 == "quit":
                print("Player 2 won the game")
                print("###### Game Succesfully Finished ######")
                quits = 1
                break
            if input_1=="roll":
                dice_value = get_dice_value()
                break
            else:
                if input_1.isdecimal():
                    if int(input_1)>=1 and int(input_1)<=20:
                        dice_value = int(input_1)
                        break
                    else:
                        print("Invalid Input. Try Again!")
                else:
                    print("Invalid Input. Try Again!")
        if quits==1:
            break
        print("You got a {}".format(dice_value))
        player1_current_position = snake_ladder(player1_current_position, dice_value)

        check = check_win("Player 1", player1_current_position)
        if check==1:
            break

        while True:
            input_2 = input("Player 2: ")
            if input_2 == "quit":
                print("Player 1 won the game")
                print("###### Game Succesfully Finished ######")
                quits = 1
                break
            if input_2=="roll":
                dice_value = get_dice_value()
                break
            else:
                if input_2.isdecimal():
                    if int(input_2)>=1 and int(input_2)<=20:
                        dice_value = int(input_2)
                        break
                    else:
                        print("Invalid Input. Try Again!")
                else:
                    print("Invalid Input. Try Again!")
        if quits==1:
            break
        print("You got a {}".format(dice_value))
        player2_current_position = snake_ladder(player2_current_position, dice_value)

        check = check_win("Player 2", player2_current_position)
        if check==1:
            break
        


if __name__ == "__main__":
    start()
