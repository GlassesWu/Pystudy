#CalPiV3.py
from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0
start = perf_counter()
for i in range(DARTS):
    x, y = random(),random()
    distance = pow((x**2 + y**2),0.5)
    if distance <= 1.0:
        hits += 1
pi = 4*(hits/DARTS)
print("圆周率值是：{0},运行时间：{1}".format(pi,perf_counter()-start))
