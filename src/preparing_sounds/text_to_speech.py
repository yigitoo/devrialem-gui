from gtts import gTTS
import os


try:
	while True:
		mytext = input("Give text for creating mp3 file: ")
		lang = "tr"

		sound = gTTS(text=mytext, lang=lang, slow=False)

		filename = input("Give file name for saving sound binary: ")
		sound.save(f"{filename}.mp3")
except KeyboardInterrupt:
	exit("\nFiles are saved!:)")