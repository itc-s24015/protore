#s24015
#turtlr1.py

from turtle import * #タートルグラフィックスを使う準備
shape("turtle")#カメの登場
col = ("orange","green","gold","blue","red","yellow","green","brown","purple","gray","indigo")
for i in range(11):
    color(col[i])
    circle(100)
    left(33)
    forward(100)
    left(33)
    

done()#おしまい

