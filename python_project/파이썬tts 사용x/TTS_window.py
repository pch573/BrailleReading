import win32com.client #윈도우 버젼일때
import Translation
from gtts import gTTS

tts = gTTS(text=Translation.TEXT, lang='ko')
i= 1
while(i):
    tts = win32com.client.Dispatch("SAPI.SpVoice")
    tts.Speak(Translation.TEXT)
    tts.Speak("다시 한번 들으시겠습니까?")
    Replay = input("Y/N :: ") #이 부분을 어떻게 처리할까?.../ ui버튼 이벤트?
    if Replay == "N" or Replay == "n":
        i = False

