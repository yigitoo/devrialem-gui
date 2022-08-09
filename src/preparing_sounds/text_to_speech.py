from gtts import gTTS
import os


try:
	while True:
		mytext = input("Give text for creating mp3 file: ")
		lang = "tr"

		sound = gTTS(text=mytext, lang=lang, slow=False)

		filename = input("Give file name for saving sound binary: ")
		sound.save(f"{filename}.mp3")
		with open('sound_transcript.txt','a', encoding='utf-8') as f:
			f.write(f'\n{filename}: {mytext}') # i am genius :D i solved it!
														  # with runepages :3 Yeah i play
														  # LoL. and i am lifeless :/ 
														  # but i am yasuo main sooo:D
except KeyboardInterrupt:
	exit("\nFiles are saved!:)")
# MP3 Files For Recovery :)
# cikis
# giris
# kayit
# kullbilgi
# merhaba