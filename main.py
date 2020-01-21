import random
import webbrowser

running = True

while running:
    video = random.choice(open("videos.txt").read().split())

    webbrowser.open_new_tab(video)

    break
