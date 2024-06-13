Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:5:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #s24015
>>> #おみくじプログラム
>>> import random
>>> print("大吉","中吉","小吉","大凶")
大吉 中吉 小吉 大凶
>>> kuji = ["大吉","中吉","小吉","大凶"]
>>> print(random.choice(kuji))
小吉
>>> 
>>> 
== RESTART: C:/Users/城間広大/AppData/Local/Programs/Python/Python312/purotore.py ==
大吉 中吉 小吉 大凶
大吉
>>> 
== RESTART: C:/Users/城間広大/AppData/Local/Programs/Python/Python312/purotore.py ==
大吉 中吉 小吉 大凶
大凶
print(random.choice(kuji))
