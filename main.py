import random
import webbrowser

running = True

while running:
    # Choose random video from videos.txt file
    video = random.choice(open("videos.txt").read().split())

    # Play video in new web browser tab
    webbrowser.open_new_tab(video)

    break
