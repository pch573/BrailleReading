import os
from gtts import gTTS #구글API사용
import Translation
import pygame
from mutagen.mp3 import MP3
import time



text_to_read = "다시 한번 들으시겠습니까?" #replay
language = 'ko' #tts 한국어로 설정
slow_audio_speed = 0 #저장할 때 재생 속도
Korean = "Korean.mp3" #번역한 mp3파일
replay_file = "replay.mpe" #replay mp3 파일

freq = 24000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
bitsize = -16   # signed 16 bit. support 8,-8,16,-16
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)

pygame.mixer.init(freq, bitsize, channels, buffer) #파이썬 내 mp3 재생 초기값 설정


i= 1
while(i):
    audio_created = gTTS(text=Translation.Hangle, lang=language, slow=slow_audio_speed) #tts 초기값 설정
    audio_created.save(Korean)        #mp3 저장
    pygame.mixer.music.load(Korean)       #mp3 재생 파일 설정
    pygame.mixer.music.play()           #mp3 파일 재생
    audio_time = MP3(Korean)          #mp3 파일 지정
    play_time = audio_time.info.length      #mp3 파일 길이
    time.sleep(play_time)           #sleep 함수로 Replay가 Korean이 끝나기 전에 재생하는 것을 방지
    print("wake up!")               #sleep 함수 정상 확인 테스트
    audio_created = gTTS(text=text_to_read, lang=language, slow=slow_audio_speed)  # tts 초기값 설정 (replay)
    audio_created.save(replay_file)  # mp3 저장
    pygame.mixer.music.load(replay_file)
    pygame.mixer.music.play()

    Replay = input("Y/N :: ")       #이 부분을 어떻게 처리할까?.../ ui버튼 이벤트?
    if Replay == "N" or Replay == "n":
        i = False
        pygame.mixer.quit()         #재생이 끝나고 close()기능






