from microbit import *

speaker.on()

adjusted_level = 10/255
def play_warning(level):
    level_adjusted_freq = 3000/255 # max light is 3000 Hz
    freq = int(level_adjusted_freq*level)
    sound = audio.SoundEffect(freq_start=freq, freq_end=freq, duration=20)
    audio.play(sound)

prev_time = running_time()
while True:
    level = display.read_light_level()
    display.show(int(level * adjusted_level))
    if level > 50:
        play_warning(level)
    elif running_time() > prev_time + 1000:
        prev_time = running_time()
        play_warning(200)
