#GUIで動くアプリを作ってみる
import tkinter as tk #まずこの行を書く必要がある

root = tk.Tk()#初めのコード

root.geometry("600x400")#運動のサイズを決める
root.title("アプリの練習")#ウインドウのタイトルを決める
lbl = tk.Label(text="hello world")#いつもの
lbl.pack() #lblを配置させる必要があるroot.mainloop()#終わりのコーdo


root.mainloop()#終わりのコード
