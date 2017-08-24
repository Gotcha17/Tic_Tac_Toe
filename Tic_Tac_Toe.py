import os
import tkFont
import tkSimpleDialog
from Tkinter import *                                   # Imports all the Tkinter elements used for GUI
from tkMessageBox import *                              # Imports all the tkMessageBox elements used for GUI

root = Tk()                                             # Creates main window
w = 400                                                 # width for the Tk root
h = 350                                                 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth()                           # width of the screen
hs = root.winfo_screenheight()                          # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))             # Sets geometry of the main window
root.wm_title('Tic Tac Toe')                            # Sets title of the main window
root.configure(background='SkyBlue1')


# Setting font
helv16 = tkFont.Font(family='Helvetica', size=16, weight=tkFont.BOLD)


# Makes dialogs appear in front of the main windows and afterwards main windows is up front
root.deiconify()
root.lift()
root.focus_force()


# Top frame for player names
topFrame = Frame(root)              # Assigns frame to main window (root)
topFrame.pack(side=TOP)             # Places frame to most top position in the main windows


# Bottom frame for player names
bottomFrame = Frame(root)           # Assigns frame to main window (root)
bottomFrame.pack(side=BOTTOM)       # Places frame to most bottom position in the main windows


# Initial variables
player_turn = 0                     # Player 1 always starts the game


# Restart the game
def restart_game():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Question dialogs in the beginning of the game that asks player names
def question(player):
    if player == 0:
        name = tkSimpleDialog.askstring("First Player's name", "What is Player 1's name?")
    else:
        name = tkSimpleDialog.askstring("Second Player's name", "What is Player 2's name?")
    return name


# End game function, tells about the outcome of the game and asks about another game
def end_game(self):
    if self == 0:
        if player_turn == 1:
            caption = player1_name['text'] + ' has won! Do you want to play again?'
        else:
            caption = player2_name['text'] + ' has won! Do you want to play again?'
    elif self == 1:
        caption = 'Game ended with a draw! Do you want to play again?'
    else:
        caption = ''
    play_again = askokcancel(title='Game ended!', message=caption)
    if play_again:
        restart_game()
    else:
        sys.exit()


# Button click function, clicked buttons text is changed to 'X' or '0' depending on which players turn it is
def button_action(button):
    if button['text'] == '':
        global player_turn
        if player_turn == 0:
            button['text'] = 'X'
            button['bg'] = 'gold'
            turn_label['text'] = '-->'
            player1_name['fg'] = 'black'
            player2_name['fg'] = 'pale green'
            player_turn = 1
        else:
            button['fg'] = 'light yellow'
            button['text'] = 'O'
            button['bg'] = 'pale green'
            turn_label['text'] = '<--'
            player1_name['fg'] = 'gold'
            player2_name['fg'] = 'black'
            player_turn = 0
        game_logic()
        return player_turn
    else:
        pass


# Game logic function, checks whether one of the players has won after his move or a draw has occurred
def game_logic():
    index = list()
    index.append(b0['text'])
    index.append(b1['text'])
    index.append(b2['text'])
    index.append(b3['text'])
    index.append(b4['text'])
    index.append(b5['text'])
    index.append(b6['text'])
    index.append(b7['text'])
    index.append(b8['text'])
    win_identification = ''
    for value in range(0, 3):
        win_identification = win_identification + index[value]
        if win_identification.count('X') == 3 or win_identification.count('O') == 3:
            end_game(0)
    else:
        win_identification = ''
        for value in range(3, 6):
            win_identification = win_identification + index[value]
            if win_identification.count('X') == 3 or win_identification.count('O') == 3:
                end_game(0)
        else:
            win_identification = ''
            for value in range(6, 9):
                win_identification = win_identification + index[value]
                if win_identification.count('X') == 3 or win_identification.count('O') == 3:
                    end_game(0)
            else:
                win_identification = ''
                for value in range(0, 9, 3):
                    win_identification = win_identification + index[value]
                    if win_identification.count('X') == 3 or win_identification.count('O') == 3:
                        end_game(0)
                else:
                    win_identification = ''
                    for value in range(1, 9, 3):
                        win_identification = win_identification + index[value]
                        if win_identification.count('X') == 3 or win_identification.count('O') == 3:
                            end_game(0)
                    else:
                        win_identification = ''
                        for value in range(2, 9, 3):
                            win_identification = win_identification + index[value]
                            if win_identification.count('X') == 3 or win_identification.count('O') == 3:
                                end_game(0)
                        else:
                            win_identification = ''
                            for value in range(0, 9, 4):
                                win_identification = win_identification + index[value]
                                if win_identification.count('X') == 3 or win_identification.count('O') == 3:
                                    end_game(0)
                            else:
                                win_identification = ''
                                for value in range(2, 7, 2):
                                    win_identification = win_identification + index[value]
                                    if win_identification.count('X') == 3 or win_identification.count('O') == 3:
                                        end_game(0)
                                else:
                                    if (index.count('X') + index.count('O')) >= 9:
                                        end_game(1)


# Initialization of dialog boxes for player names
player1_caption = question(0)
player2_caption = question(1)

# Labels
player1_name = Label(topFrame, text=player1_caption, width=10, height=2, fg='gold', bg='SkyBlue1', font=helv16)
player1_name.grid(row=0, column=0)

player2_name = Label(topFrame, text=player2_caption,  width=10, height=2, bg='SkyBlue1', font=helv16)
player2_name.grid(row=0, column=2)

turn_label = Label(topFrame, text='Have Fun!',  width=10, height=2, bg='SkyBlue1', font=helv16)
turn_label.grid(row=0, column=1)


# Buttons
b0 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b0))
b0.grid(row=0, column=0)

b1 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b1))
b1.grid(row=0, column=1)

b2 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b2))
b2.grid(row=0, column=2)

b3 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b3))
b3.grid(row=1, column=0)

b4 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b4))
b4.grid(row=1, column=1)

b5 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b5))
b5.grid(row=1, column=2)

b6 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b6))
b6.grid(row=2, column=0)

b7 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b7))
b7.grid(row=2, column=1)

b8 = Button(bottomFrame, text='', width=5, height=3, font=helv16, bg='SkyBlue1', command=lambda: button_action(b8))
b8.grid(row=2, column=2)

root.mainloop()


