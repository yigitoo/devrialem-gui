import threading
import os
import time
from functools import partial

def voice_exec(filename):
    if os.name == "nt":
        os.system(f'vlc -Idummy  .\\preparing_sounds\\{filename}.mp3')
    if os.name == "posix":
        os.system(f'mpg123 ./preparing_sounds/{filename}.mp3')

def play_voice(filename):
    xVoiceExec = partial(voice_exec, filename)
    thread_runVoice = threading.Thread(target=xVoiceExec)
    time.sleep(1.5)
    thread_runVoice.start()

if __name__ == '__main__':
    play_voice('merhaba')