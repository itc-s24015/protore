#turtlr1.py

from turtle import * #タートルグラフィックスを使う準備
shape("turtle")#カメの登場
col = ("orange","green","gold","blue","red",)
for i in range(5):
    color(col[i])
    forward(200)
    left(144)

done()#おしまい

