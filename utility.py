import time

cur_time = time.time()
prev_time = time.time()

def timeTick():
    global cur_time, prev_time
    cur_time = time.time()
    elapsedTime = cur_time - prev_time
    prev_time = cur_time
    return elapsedTime