from moneyBack import *
import time

start = time.time()
amount = whichCoinsDoIGive(10, [1,2,3])
print(time.time()-start, amount)
start = time.time()
amount = change_possibilities_bottom_up(100, [1,2,3])
print(time.time()-start, amount)

#4-1-1
#3-3
#3-2-1
#3-1-1-1
#2-2-2
#2-2-1-1
#2-1-1-1-1
#1-1-1-1-1-1