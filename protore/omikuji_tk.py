#s24015
#おみくじをGUIで動かすプログラム
import tkinter as tk
import random
root = tk.Tk()

root.geometry("600x400")
root.title("おみくじ")
kuji=["大吉","中吉","小吉","大凶"]
lbl=tk.Label(text=(random.choice(kuji)))
lbl.pack()
 

root.mainloop()
