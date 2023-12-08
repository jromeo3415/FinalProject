import os.path
from pydub import AudioSegment


def checkType(file):    #needs to be changed so the file is changed at the location it is at instead of returning an object (already did?)
    fileExtension = os.path.splitext(file)
    if fileExtension == ".wav":
        return file
    elif fileExtension == ".mp3":
        temp = AudioSegment.from_mp3(file)
        temp.export(file.path, format='wav')
        print(temp)
        return temp
    elif fileExtension == ".aac":
        temp = AudioSegment.from_mp3(file)
        temp.export(file.path, format='wav')
        print(temp)
        return temp
    else:
        print("Incompatible file type")
        return