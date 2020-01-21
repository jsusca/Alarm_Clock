import random
import webbrowser
import re

# Play video in new web browser tab
# webbrowser.open_new_tab(video)

running = True

while running:
    # Choose random video from videos.txt file
    video = random.choice(open("videos.txt").read().split())

    alarm = input("Please enter alarm in the following format: 13:30 hour:minute")
    alarm = re.sub(r'[^:\d]+', '', alarm)

    print(alarm)

    # Alarm time in sec - current time in sec = sec to sleep
