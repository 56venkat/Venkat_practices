import webbrowser
import time

# URL of the YouTube video
video_url = "https://youtu.be/Euk3us16_b8"

# Number of times to play the video
repeat_count = 20

for _ in range(repeat_count):
    webbrowser.open(video_url)
    # Wait for the video to finish before opening the next one
    # This assumes the video length is 3 minutes (180 seconds)
    time.sleep(180)
