import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def find_target_frequency(freq_band):
    for x in freqs:
        if x > freq_band:
            break
    return x

def frequency_check(freq_band):
    target_frequency = find_target_frequency(freq_band)
    index_of_frequency = np.where(freqs == target_frequency)[0][0]
    data_for_frequency = spectrum[index_of_frequency]
    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun

def find_nearest_value(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def plotrt60(file_path, freq_band, freq_name):
    sample_rate, data = wavfile.read(file_path)  #put in file path
    global spectrum, freqs, t, im
    spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

    data_in_db = frequency_check(freq_band)
    plt.figure()
    plt.title(freq_name)
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color ='#004bc6')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (dB)')

    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

    sliced_array = data_in_db[index_of_max:]

    value_of_max_less_5 = value_of_max - 5



    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)

    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
    rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]

    rt60 = rt20 * 3

    plt.grid()
    plt.show()