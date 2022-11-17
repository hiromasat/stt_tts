import argparse
import os

import speech_recognition as sr


def speechrecognition(audiofile_path):
    r = sr.Recognizer()
    with sr.AudioFile(audiofile_path) as source:
        audio = r.record(source)
    text = r.recognize_google(audio, language='ja-JP')
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('audiofile_path', help='Path to audio file')
    args = parser.parse_args()
    audiofile_path = args.audiofile_path

    if os.path.exists(audiofile_path) and audiofile_path.endswith('.wav'):
        text = speechrecognition(audiofile_path)
        print(text)
    else:
        print('ファイルを指定してください。')
