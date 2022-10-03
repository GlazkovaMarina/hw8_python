from datetime import datetime as dt
from time import time
def log(mode, data):
    with open("log.txt", "a") as f:
        time = dt.now().strftime('%H.%M')
        date = str(dt.now().day) + '.' + str(dt.now().month) + "." + str(dt.now().year)
        line = mode + ": " + date + " " + time + ": " + data + "\n"
        f.write(line)