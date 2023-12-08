import matplotlib.pyplot as plt
import numpy as np

def plotAll(length, file_path):
    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data[:, 0])
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()