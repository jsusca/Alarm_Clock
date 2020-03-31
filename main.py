import random
import time
import webbrowser
import re


running = True

while running:
    # Choose random video from videos.txt file
    video = random.choice(open("videos.txt").read().split())

    # Take user input and scrub
    alarm = input("Please enter alarm in the following format: 13:30 hour:minute\n")
    alarm = re.sub(r'[^:\d]+', '', alarm)
    if alarm == '':
        continue

    # Split 24h time into hours and minutes
    alarm = alarm.split(':')

    # Convert hours and minutes into seconds (based on 24hours)
    alarm_seconds = (int(alarm[0]) * 60 * 60) + (int(alarm[1]) * 60)

    # Set current_time equal to local time
    current_time = time.strftime('%X', time.localtime())

    # Split current_time into hours and minutes
    current_time = current_time.split(':')

    # Convert current_time into seconds (based on 24 hours)
    current_time_seconds_day = (int(current_time[0]) * 60 * 60) + (int(current_time[1]) * 60) + int(current_time[2])

    # If alarm is set for later today:
    if alarm_seconds > current_time_seconds_day:
        # Alarm time in sec - current time in sec = sec to sleep
        sleep_time = alarm_seconds - current_time_seconds_day

    # If alarm is set for current time, reset program
    if alarm_seconds == current_time_seconds_day:
        continue

    # If alarm is set for tomorrow:
    if alarm_seconds < current_time_seconds_day:
        sleep_time = (86400 - current_time_seconds_day)
        sleep_time += alarm_seconds

    print(sleep_time)
    print(time.gmtime(sleep_time))

    # Suspend execution for sleep_time
    time.sleep(sleep_time)

    # Play video in new web browser tab
    webbrowser.open_new_tab(video)


