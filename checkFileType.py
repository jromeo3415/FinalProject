import os.path
from pydub import AudioSegment


def checkType(file):
    fileExtension = os.path.splitext(file)
    if fileExtension == ".wav":
        return file
    elif fileExtension == ".mp3":
        temp = AudioSegment.from_mp3(file)
        temp.export(temp, format='wav')
        print(temp)
        return temp