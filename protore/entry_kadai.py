#s24015 entry_kadai,py
#エントリーウィジェットで受け付けた金額を税込み（１０％）価格としてだす
import tkinter as tk #tkinterをtkと略して使用する

def dispLabel():
    a = entry.get()
    print(f"aは{type(a)}")
    lbl.config(text=f"{a}さんこんにちは")
#print("金額を入力してください")
#a = input()
#print(type(a))


root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400×200")
#面の大きさを決める

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn= tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
