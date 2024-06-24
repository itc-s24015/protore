#s24015
#実行が確認出来たら時間を表示させる「時間アプリ」を作ってみたいと思います
#時計アプリはモジュールを「time_kadai.py]で作成します
#時計アプリを使いやすくバージョンアップしていきます

import datetime
import tkinter as tk #GUIでアプリをを作ることができるモジュール

#時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%s秒")
    lbl.config(text=current_time)
    root.after(1000,update_time)
#Tkinterのウィンドウを作成
root = tk.Tk()

root.title("現在の時刻")
 
lbl = tk.Label()
lbl.config(text="",font=("Helventica",20))
lbl.pack()
            

    #関数の呼び出し 
update_time()

root.mainloop()
