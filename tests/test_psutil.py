import psutil
import time

while True:
    print("flexsim.exe" in (p.name() for p in psutil.process_iter()))
    time.sleep(1)