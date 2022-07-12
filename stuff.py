import os

def draw_board(spots):
    board = (f"| {spots[1]} | {spots[2]} | {spots[3]} |\n"
                f"-------------\n"
                f"| {spots[4]} | {spots[5]} | {spots[6]} |\n"
                f"-------------\n"
                f"| {spots[7]} | {spots[8]} | {spots[9]} |")

    print(board) 

def check_turn(turn):
    if turn % 2 == 0: return '0'
    else: return 'X'

def check_for_win(spots):
    if (spots[1] == spots[2] == spots[3]) \
     or (spots[4] == spots[5] == spots[6]) \
     or (spots[7] == spots[8] == spots[9]):
     return True

    elif (spots[1] == spots[4] == spots[7]) \
     or (spots[2] == spots[5] == spots[8]) \
     or (spots[3] == spots[6] == spots[9]):
     return True

    elif (spots[1] == spots[5] == spots[9]) \
     or (spots[3] == spots[5] == spots[7]):
     return True

    else: return False   

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
        6 : '6', 7 : '7', 8 :'8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots) 
    if prev_turn == turn:
      print("Laukelis užimtas, pasirinkite kitą.")
    prev_turn = turn
    print("Žaidėjas " + str((turn % 2) +1 ) + " eilė: pasirinkite laukelį arba paspauskite q baigti žaidimą.")
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
      if not spots[int(choice)] in {"X", "O"}:
          turn += 1
          spots[int(choice)] = check_turn(turn) 

if check_for_win(spots): playing, complete = False, True
if turn > 8: playing = False


os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete:
    if check_turn(turn) == 'X': print("Žaidėjas 2 laimėjo!")
    else: print("Žaidėjas 2 laimėjo!")

else:
    print("Laimėtojo nėra")

print("Ačiū, kad žaidėte!")
import os

def draw_board(spots):
    board = (f"| {spots[1]} | {spots[2]} | {spots[3]} |\n"
                f"-------------\n"
                f"| {spots[4]} | {spots[5]} | {spots[6]} |\n"
                f"-------------\n"
                f"| {spots[7]} | {spots[8]} | {spots[9]} |")

    print(board) 

def check_turn(turn):
    if turn % 2 == 0: return '0'
    else: return 'X'

def check_for_win(spots):
    if (spots[1] == spots[2] == spots[3]) \
     or (spots[4] == spots[5] == spots[6]) \
     or (spots[7] == spots[8] == spots[9]):
     return True

    elif (spots[1] == spots[4] == spots[7]) \
     or (spots[2] == spots[5] == spots[8]) \
     or (spots[3] == spots[6] == spots[9]):
     return True

    elif (spots[1] == spots[5] == spots[9]) \
     or (spots[3] == spots[5] == spots[7]):
     return True

    else: return False   

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
        6 : '6', 7 : '7', 8 :'8', 9 : '9'}


playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots) 
    if prev_turn == turn:
      print("Laukelis užimtas, pasirinkite kitą.")
    prev_turn = turn
    print("Žaidėjas " + str((turn % 2) +1 ) + " eilė: pasirinkite laukelį arba paspauskite q baigti žaidimą.")
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
      if not spots[int(choice)] in {"X", "O"}:
          turn += 1
          spots[int(choice)] = check_turn(turn) 

if check_for_win(spots): playing, complete = False, True
if turn > 8: playing = False


os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete:
    if check_turn(turn) == 'X': print("Žaidėjas 2 laimėjo!")
    else: print("Žaidėjas 2 laimėjo!")

else:
    print("Laimėtojo nėra")

print("Ačiū, kad žaidėte!")
