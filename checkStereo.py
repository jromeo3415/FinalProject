from pydub import AudioSegment

def checkStereo(file):
    raw_audio = AudioSegment.from_file(file, format="wav")
    mono_audio = raw_audio.set_channels(1)
    mono_audio.export(file, format="wav")