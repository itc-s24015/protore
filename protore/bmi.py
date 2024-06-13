#24015
#BMI値計算プログラム

h = float(input("身長は何センチですか？")) / 100.0
w = float(input("体重は何キロですか?"))

bmi = w / (h * h)
print("あなたのBMI値は、",bmi,"です。")
