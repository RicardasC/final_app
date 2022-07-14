from tkinter import * 
from tkinter import messagebox

window = Tk()
window.title('Tik Tak Toe')
window.geometry('623x651')


clicked = True
count = 0

def finalwinner():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green"), b2.config(bg="green"), b3.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green"), b5.config(bg="green"), b6.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")
        
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green"), b8.config(bg="green"), b9.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green"), b4.config(bg="green"), b7.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green"), b5.config(bg="green"), b8.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green"), b6.config(bg="green"), b9.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green"), b5.config(bg="green"), b9.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green"), b5.config(bg="green"), b7.config(bg="green")
        winner = True
        messagebox.askyesno("X Laimėjo", "Ar bandysite dar kartą?")

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green"), b2.config(bg="green"), b3.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green"), b5.config(bg="green"), b6.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")
        
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green"), b8.config(bg="green"), b9.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green"), b4.config(bg="green"), b7.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green"), b5.config(bg="green"), b8.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green"), b6.config(bg="green"), b9.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green"), b5.config(bg="green"), b9.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green"), b5.config(bg="green"), b7.config(bg="green")
        winner = True
        messagebox.askyesno("O Laimėjo", "Ar bandysite dar kartą?")

    if count == 9 and winner == False:
        root.configure(bg='blue')
        messagebox.askyesno("Lygiosios", "Ar bandysite dar kartą?")

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        finalwinner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        finalwinner()
    else:
        messagebox.showerror("Tik Tak Toe", "Langelis užimtas, bandykite kitą")

b1 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, relief="sunken", bg="cornflowerblue", command = lambda: b_click(b1))
b2 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, bg="lightgoldenrod1", command = lambda: b_click(b2))
b3 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, relief="sunken", bg="cornflowerblue", command = lambda: b_click(b3))

b4 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, bg="lightgoldenrod1", command = lambda: b_click(b4))
b5 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, relief="sunken", bg="cornflowerblue", command = lambda: b_click(b5))
b6 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, bg="lightgoldenrod1", command = lambda: b_click(b6))

b7 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, relief="sunken", bg="cornflowerblue", command = lambda: b_click(b7))
b8 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, bg="lightgoldenrod1", command = lambda: b_click(b8))
b9 = Button(window, text= " ", font=("arial", 80, "bold"), height=1, width=3, relief="sunken", bg="cornflowerblue", command = lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

window.mainloop()
