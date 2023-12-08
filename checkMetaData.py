from pydub import AudioSegment

def checkMetaData(file):
    audio = AudioSegment.from_file(file)

    print("Audio Info:")
    print(f"Channels: {audio.channels}")
    print(f"Sample Width: {audio.sample_width} bytes")
    print(f"Frame Rate: {audio.frame_rate} Hz")
    print(f"Frame Width: {audio.frame_width} bytes")
    print(f"Length: {len(audio)} milliseconds")