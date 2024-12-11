import random as r 
import time

for i in range (15):
    print("Espere un momento mientras generamos un numero...")
    time.sleep(2)
    print(r.randint(1,10))
