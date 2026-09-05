import time
import vlc  # python-vlc package

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

# Alarm sound - yahan apni file ka path ya URL do
player = vlc.MediaPlayer("mixkit-facility-alarm-sound-999.wav")  # ya koi bhi mp3/wav file
player.play()

# Sound khatam hone tak wait karo
while player.is_playing():
    time.sleep(0.1)

print("Time's up! 🔊")