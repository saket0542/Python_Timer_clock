import time
import simpleaudio as sa


def alarm(seconds):
    time_elasped = 0
    while time_elasped < seconds:
        time.sleep(1)
        time_elasped += 1
        time_left = seconds - time_elasped
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{minutes_left:02d}:{seconds_left:02d}")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
wave_obj = sa.WaveObject.from_wave_file("alarm-sound.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
