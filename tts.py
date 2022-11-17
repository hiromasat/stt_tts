import argparse

import pyttsx3
from gtts import gTTS
from playsound import playsound


def tts_pyttsx3(text, filename):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)

    # ファイル生成ができない
    # engine.save_to_file(text, f'speech_{filename}.mp3')
    engine.say(text)
    engine.runAndWait()

def tts_gTTS(text, filename):
    tts = gTTS(text=text, lang="ja")
    tts.save(f'speech_{filename}.mp3')
    playsound(f'speech_{filename}.mp3')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('textfile_path', help='Text file to speech')
    parser.add_argument('engine', help='engine for tts')
    args = parser.parse_args()

    with open(args.textfile_path, encoding="utf-8") as f:
        text = f.read()

    if args.engine == 'gTTS':
        tts_gTTS(text, 'gTTS')
    elif args.engine == 'pttsx3':
        tts_pyttsx3(text, 'pttsx3')
    else:
        print('適切なエンジンを指定してください')
