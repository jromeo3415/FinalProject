import os.path
from pydub import AudioSegment


def checkType(file):    #needs to be changed so the file is changed at the location it is at instead of returning an object (already did?)
    fileExtension = os.path.splitext(file)[1]
    if fileExtension == ".WAV":
        return
    elif fileExtension == ".mp3":
        temp = AudioSegment.from_mp3(file)
        temp.export(file, format='wav')
        print(temp)
        return
    elif fileExtension == ".aac":
        temp = AudioSegment.from_mp3(file)
        temp.export(file, format='wav')
        print(temp)
        return
    else:
        print("Incompatible file type")
        return

def checkMetaData(file):
    audio = AudioSegment.from_file(file)

    print("Audio Info:")
    print(f"Channels: {audio.channels}")
    print(f"Sample Width: {audio.sample_width} bytes")
    print(f"Frame Rate: {audio.frame_rate} Hz")
    print(f"Frame Width: {audio.frame_width} bytes")
    print(f"Length: {len(audio)} milliseconds")

def checkStereo(file):
    raw_audio = AudioSegment.from_file(file, format="wav")
    mono_audio = raw_audio.set_channels(1)
    mono_audio.export(file, format="wav")