import os.path
from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np

def checkType(file):    #checks file extension and changes it if needed
    fileExtension = os.path.splitext(file)[1]
    if fileExtension == ".WAV":
        return
    elif fileExtension == ".mp3":
        temp = AudioSegment.from_mp3(file)
        temp.export(file, format='wav')
        print(temp)
        return
    elif fileExtension == ".aac":
        temp = AudioSegment.from_file(file, format='aac') #needs to be changed to aac not mp3
        temp.export(file, format='wav')
        print(temp)
        return
    else:
        print("Incompatible file type")
        return

def checkMetaData(file):    #prints out metadata related to the sound file
    audio = AudioSegment.from_file(file)

    print("Audio Info:")
    print(f"Channels: {audio.channels}")
    print(f"Sample Width: {audio.sample_width} bytes")
    print(f"Frame Rate: {audio.frame_rate} Hz")
    print(f"Frame Width: {audio.frame_width} bytes")
    print(f"Length: {len(audio)} milliseconds")
    return len(audio)

def checkStereo(file):  #converts to monophonic
    raw_audio = AudioSegment.from_file(file, format="wav")
    mono_audio = raw_audio.set_channels(1)
    mono_audio.export(file, format="wav")

def makeWavArray(file_path):    #used to obtain an array of values to plot waveform
    data = wavfile.read(file_path)
    data = np.array(data[1], dtype=np.float32)
    normalized_data = data / np.max(np.abs(data), axis=0)
    return normalized_data