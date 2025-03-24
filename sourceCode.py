import random
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


def home_page(pre):
    pre.destroy()
    root = tk.Tk()
    root.geometry("500x600")
    root.title("Tic Tac Toe")
    root.configure(background='#2a2e30')

    # Logo Settting
    original_image = Image.open("Tic logo.png")
    resized_image = original_image.resize((400, 400), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    bg_label = tk.Label(root, image=bg_image , bg='#2a2e30')
    bg_label.place(x = 55) 

    #button setting
    Player2 = Button (root, text = "With a Friend", bg = "#6d70c3", fg = "#EAEBED", font = "Helvetica",  relief="raised" , width = 15, height = 2 ,  command=lambda: Player2UI(root)) 
    Player2.place(x = 166, y = 320)

    Computer = Button (root, text = "With a Computer", bg = "#d1d3f3", fg = "#2a2e30", font = "Helvetica",  relief="raised" , width = 17, height = 2 ,  command=lambda: ComputerUI(root) )
    Computer.place(x = 155, y = 400)
    root.mainloop()

def ComputerUI(root):
    root.destroy()
    Computerui = tk.Tk()
    Computerui.geometry("500x600")
    Computerui.title("Tic Tac Toe")
    Computerui.configure(background='#2a2e30')
    

    canvas = Canvas(Computerui, bg = "#2a2e30")
    canvas.pack(expand=True, fill=BOTH)
    bt_x = Image.open("4.png")
    bt_o = Image.open("3.png")
    Computerui.bt_x = ImageTk.PhotoImage(bt_x.resize((300, 300), Image.LANCZOS))
    Computerui.bt_o = ImageTk.PhotoImage(bt_o.resize((300, 300), Image.LANCZOS))
   
    o_label = Label (Computerui , image = Computerui.bt_o, bg = "#2a2e30" ,  width = 120, height = 120 , bd=0  , activebackground="#2a2e30" )
    x_label = Label (Computerui , image = Computerui.bt_x, bg = "#2a2e30" ,  width = 120, height = 120 , bd=0  , activebackground="#2a2e30" )
    canvas.create_window(180, 250, window=x_label)
    canvas.create_window(330, 250, window=o_label)

    promot = Label(Computerui, text = "Pick your side", bg = "#2a2e30", fg = "#e0e1dd", font = "Helvetica 20 bold")
    promot.place(x = 160, y = 100)

    

    def display():
        print('the value associated to the selected radio button: ', selected_side.get())

    selected_side = IntVar()
    rx = Radiobutton(Computerui, text="", variable=selected_side, value=1 , bg = "#2a2e30" , fg = "#6d70c3" ,command=display)
    ro = Radiobutton(Computerui, text="", variable=selected_side, value=2 , bg = "#2a2e30" , fg = "#6d70c3" ,command=display)
    rx.place (x = 160, y = 350)
    ro.place (x = 320, y = 350)
    selected_side.set(1)

    play_bt = Button (Computerui, text = "Ready!" ,bg = "#6d70c3", fg = "#EAEBED", font = "Helvetica",  relief="raised" , width = 13, height = 1 ,command=lambda: start_play(Computerui , selected_side))
    play_bt.place(x = 170 , y = 430)
    back = Button(Computerui, text="Back",  bg = "#d1d3f3", fg = "#2a2e30", font = "Helvetica ",  relief="raised" , width = 13, height = 1 , command=lambda: home_page(Computerui))
    back.place(x = 170 , y = 490)
    Computerui.mainloop()

def check_win(board):
        """التحقق من وجود فائز"""
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        return None

def empty_board(row , col , board):
    if board[row][col] == " ":
        return True
    else:
        return False
    
def check_draw(board):
        return all(board[r][c] != " " for r in range(3) for c in range(3))

def disable_buttons(buttons):
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(state="disabled")

def click(row, col, player, computer , label, gameui, board, buttons,colors):
        if board[row][col] == " ":
            board[row][col] = player
            buttons[row][col].config(text=player ,fg=colors[player] )

            if check_win(board) == player:
                label["text"] = f"{player} Wins!"
                disable_buttons(buttons)
                messagebox.showinfo("Game Over", f"Player ({player}) Wins!")
                return

            if check_draw(board):
                label["text"] = "It's a Draw!"
                messagebox.showinfo("Game Over", "The game is a draw!")
                return

            label["text"] = f"{computer}'s Turn"
            gameui.after(500, lambda: computer_move(label, player, computer,board, buttons,colors)) 

        else:
            messagebox.showwarning("Invalid Move", "This spot is already taken!")

def friend_click(row, col, player1, player2, label, board, buttons,colors , current_player):
        if board[row][col] == " ":
            board[row][col] = current_player[0]
            buttons[row][col].config(text=current_player[0], fg=colors[current_player[0]])
            

            if check_win(board) == current_player[0]:
                label.config(text=f"{current_player[0]} Wins!")
                disable_buttons(buttons)
                messagebox.showinfo("Game Over", f"Player ({current_player[0]}) Wins!")
                return

            if check_draw(board):
                label.config(text="It's a Draw!")
                messagebox.showinfo("Game Over", "The game is a draw!")
                return
            
            current_player[0] = player2 if current_player[0] == player1 else player1
            label.config(text=f"{current_player[0]}'s Turn")
        else:
            messagebox.showwarning("Invalid Move", "This spot is already taken!")

# def computer_move(label, player, computer,board, buttons,colors):
#         empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
#         if empty_cells:
#             r, c = random.choice(empty_cells)
#             board[r][c] = computer
#             buttons[r][c].config(text=computer , fg=colors[computer])

#             if check_win(board) == computer:
#                 label["text"] = f"{computer} Wins!"
#                 disable_buttons(buttons)
#                 messagebox.showinfo("Game Over", f"Computer ({computer}) Wins!")
#                 return

#             if check_draw(board):
#                 label["text"] = "It's a Draw!"
#                 messagebox.showinfo("Game Over", "The game is a draw!")
#                 return

#             label["text"] = f"{player}'s Turn"

def computer_move(label, player, computer, board, buttons, colors):
    def can_win(brd, mark):

        for r in range(3):
            for c in range(3):
                if brd[r][c] == " ":
                    brd[r][c] = mark
                    if check_win(brd) == mark:
                        brd[r][c] = " "
                        return (r, c)
                    brd[r][c] = " "
        return None

    win_move = can_win(board, computer)
    if win_move:
        r, c = win_move
    else:

        block_move = can_win(board, player)
        if block_move:
            r, c = block_move
        else:

            if board[1][1] == " ":
                r, c = 1, 1
            else:
                corners = [(0,0), (0,2), (2,0), (2,2)]
                empty_corners = [pos for pos in corners if board[pos[0]][pos[1]] == " "]
                if empty_corners:
                    r, c = empty_corners[0]  
                else:

                    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
                    if empty_cells:
                        r, c = empty_cells[0]

    board[r][c] = computer
    buttons[r][c].config(text=computer, fg=colors[computer])

    # التحقق من الفوز أو التعادل
    if check_win(board) == computer:
        label["text"] = f"{computer} Wins!"
        disable_buttons(buttons)
        messagebox.showinfo("Game Over", f"Computer ({computer}) Wins!")
        return

    if check_draw(board):
        label["text"] = "It's a Draw!"
        messagebox.showinfo("Game Over", "The game is a draw!")
        return

    label["text"] = f"{player}'s Turn"


def start_play(Computerui, selected_side):
    Computerui.destroy()
    gameui = tk.Tk()
    gameui.geometry("500x600")
    gameui.title("Tic Tac Toe")
    gameui.configure(background='#2a2e30')

    player = "X" if selected_side.get() == 1 else "O"
    computer = "O" if player == "X" else "X"
    
    colors = {player: "#6d70c3", computer: "#d1d3f3"}

    board = [[" " for _ in range(3)] for _ in range(3)]  
    buttons = [[None for _ in range(3)] for _ in range(3)]  


    label = tk.Label(gameui, text=f"{player}'s Turn", bg="#2a2e30", fg="white", font="Helvetica 20")
    label.pack()

    frame = tk.Frame(gameui, width=500, height=500, bg="#2a2e30")
    frame.pack()

    for r in range(3):
        for c in range(3):
            btn = tk.Button(frame, text=" ", bg="#2a2e30", font="Consolas 40 bold",
                            width=4, height=1, command=lambda row=r, col=c: click(row, col, player, computer , label, gameui, board, buttons,colors))
            btn.grid(row=r, column=c)
            buttons[r][c] = btn

    if computer == "X":
        gameui.after(500, computer_move(label, player, computer,board, buttons,colors))

    back = Button(gameui, text="Back",  bg = "#6d70c3", fg = "#EAEBED", font = "Helvetica 20 bold",  relief="raised" , width = 13, height = 1 , command=lambda: ComputerUI(gameui))
    back.place(x = 130 , y = 500)
    gameui.mainloop()



def Player2UI(root):
    root.destroy()
    gameui = tk.Tk()
    gameui.geometry("500x600")
    gameui.title("Tic Tac Toe")
    gameui.config(background='#2a2e30')

    player1 = "X"
    player2 = "O" 
    colors = {player1: "#6d70c3", player2: "#d1d3f3"}

    board = [[" " for _ in range(3)] for _ in range(3)]  
    buttons = [[None for _ in range(3)] for _ in range(3)] 

    current_player = [player1]

    label = tk.Label(gameui, text=f"{player1}'s Turn", bg="#2a2e30", fg="white", font="Helvetica 20")
    label.pack()

    frame = tk.Frame(gameui, width=500, height=500, bg="#2a2e30")
    frame.pack()
    
    for r in range(3):
        for c in range(3):
            btn = tk.Button(frame, text=" ", bg="#2a2e30", font="Consolas 40 bold",
                            width=4, height=1, command=lambda r=r, c=c: friend_click(r, c, player1, player2, label, board, buttons,colors , current_player))
            btn.grid(row=r, column=c)
            buttons[r][c] = btn

    back = Button(gameui, text="Back",  bg = "#6d70c3", fg = "#EAEBED", font = "Helvetica 20 bold",  relief="raised" , width = 13, height = 1 , command=lambda: home_page(gameui))
    back.place(x = 130 , y = 500)
    gameui.mainloop()

home_page(tk.Tk())
