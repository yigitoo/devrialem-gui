import threading
import os
import time
from functools import partial
import time
from gtts import gTTS
import shutil

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

def convert_tr_chars_to_en_and_do_it_lower_case(string): # why this functions name is so long :D
    #old/deprecated func but it'll be useful in future. So it can be stay. :D
    prev_chars =    ["ş",
                     "ç",
                     "ö",
                     "ğ",
                     "ü",
                     "ı",
                     "Ş",
                     "Ç",
                     "Ö",
                     "Ğ",
                     "Ü",
                     "İ"]
    # i am crying for this tidy situation it is seem so beautiful :')
    next_chars =   [ "s",
                     "c",
                     "o",
                     "g",
                     "u",
                     "i",
                     "S",
                     "C",
                     "O",
                     "G",
                     "U",
                     "I"]
    for i in range(12):
        string = string.replace(prev_chars[i],next_chars[i])
    return string.lower()

def voice_exec_from_path(path):
    if os.name == "nt":
        os.system("vlc -Idummy {path_expression}".format(path_expression = path.replace('/', '\\')))
        # f-strings cannot include a backslash bla bla :/
    if os.name == "posix":
        os.system(f"mpg123 {path}")

def play_voice_from_path(path):
    xVoiceExecFromPath = partial(voice_exec_from_path, path)
    thread_runVoiceFromPath = threading.Thread(target=xVoiceExecFromPath)
    time.sleep(1.5)
    thread_runVoiceFromPath.start()

def custom_voice_for_names(name):
    mytext = f"Ana menüye hoş geldin {name}!"
    lang = "tr"
    sound = gTTS(text=mytext, lang=lang, slow=False)

    sound.save('temp.mp3')
    
    if os.name == "nt":
        shutil.move('temp.mp3', f'.\\preparing_sounds\\temp.mp3')
    if os.name == "posix":
        shutil.move('temp.mp3', f'./preparing_sounds/temp.mp3')
# for trying sounds
if __name__ == '__main__':
    play_voice('merhaba')