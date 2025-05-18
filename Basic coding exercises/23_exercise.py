# 23. Create a simple countdown timer using a while loop.

import time

def timer(n):
    while n > 0:
        print(f"Time remaining : {n} seconds")
        time.sleep(1)
        n -= 1
    print("Time's up!")

timer(5)