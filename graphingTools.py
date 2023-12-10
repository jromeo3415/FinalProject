import matplotlib.pyplot as plt
import numpy as np
import librosa
from scipy.io import wavfile

def plotAll(length, wavArray):
    time = np.linspace(0., length, wavArray.shape[0])
    plt.plot(time, wavArray)
    plt.title('Waveform')
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

def calculatert60(filePath, lowFreq, midFreq, highFreq):
    y, sr = librosa.load(filePath, sr=None)

    lowBand = librosa.filters.mel(sr=sr, n_fft=2048, fmin=lowFreq[0], fmax=lowFreq[1])
    midBand = librosa.filters.mel(sr=sr, n_fft=2048, fmin=midFreq[0], fmax=midFreq[1])
    highBand = librosa.filters.mel(sr=sr, n_fft=2048, fmin=highFreq[0], fmax=highFreq[1])

    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    lowSpec = np.dot(lowBand, D)
    midSpec = np.dot(midBand, D)
    highSpec = np.dot(highBand, D)

    rt60_low = librosa.effects.estimate_rt60(lowSpec, sr=sr)
    rt60_mid = librosa.effects.estimate_rt60(midSpec, sr=sr)
    rt60_high = librosa.effects.estimate_rt60(highSpec, sr=sr)

'''def plotrt60(rt60, freqBand):
    plt.bar(0, rt60)
    plt.title(f'RT60 for ')
    plt.xlabel('Frequency Bands')
    plt.ylabel('RT60 (seconds)')
    plt.show()'''

def plotSpectogram(filePath):
    sample_rate, data = wavfile.read(filePath)
    spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
    cbar = plt.colorbar(im)
    plt.title('Spectogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    cbar.set_label('Intensity (dB)')
    plt.show()
    return spectrum

def find_target_frequency(freqs):
    for x in freqs:
        if x > 1000:
            break
    return x

def frequency_check(freqs, spectrum):
    target_frequency = find_target_frequency(freqs)
    index_of_frequency = np.where(freqs == target_frequency)[0][0]
    data_for_frequency = spectrum[index_of_frequency]
    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun

