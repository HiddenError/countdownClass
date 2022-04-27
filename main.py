# Name: Noah R
# Date: 4/24/2022
# Project: Countdown Timer using Github
# File: countdownTimer --> main.py
#-----------------------------------------------------------------

import time

def timeCountdown(userTime):
    while userTime:
        min, secs = divmod(userTime, 60)
        timer = "{:02d}:{:20d}".format(min, secs)
        print("\r", timer, end=" ")
        time.sleep(1)
        userTime -= 1
userTime = input("Please enter the time in seconds:\n")
timeCountdown(int(userTime))