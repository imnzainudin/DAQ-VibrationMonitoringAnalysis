from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from scipy.fftpack import fft
import os


def frequency(request):
    path = '/Users'
    path = os.path.join(path, 'User/Desktop/ImanZainudin', 'Online_DAQ.csv')
    df = pd.read_csv(path)
    df = df.fillna("")
    t = df["TimeEpoch"]
    x = df["xaccelaration"]
    y = df["yaccelaration"]
    z = df["zaccelaration"]

    #Variables
    N = np.int(np.prod(t.shape))
    N2 = 2**(N.bit_length()-1)
    Fs = 1/(t[1]-t[0])
    T = 1/Fs

    #Compute RMS
    #w = np.int(np.floor(Fs)); #width of the window for computing RMS
    #steps = np.int_(np.floor(N/w)); #Number of steps for RMS
    #t_RMS = np.zeros((steps,1)); #Create array for RMS time values
    #x_RMS = np.zeros((steps,1)); #Create array for RMS values
    #y_RMS = np.zeros((steps,1));
    #z_RMS = np.zeros((steps,1));
    #for i in range (0, steps):
    #    t_RMS[i] = np.mean(t[(i*w):((i+1)*w)]);
    #    x_RMS[i] = np.sqrt(np.mean(x[(i*w):((i+1)*w)]**2));
    #    y_RMS[i] = np.sqrt(np.mean(y[(i*w):((i+1)*w)]**2));
    #    z_RMS[i] = np.sqrt(np.mean(z[(i*w):((i+1)*w)]**2));

    #Compute FFT
    N = N2  # truncate array to the last power of 2
    tf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    xff = fft(x.values, n=N)
    yff = fft(y.values, n=N)
    zff = fft(z.values, n=N)
    plt.plot(tf, 2.0/N * np.abs(xff[0:np.int(N/2)]), label="x")
    plt.plot(tf, 2.0/N * np.abs(yff[0:np.int(N/2)]), label="y",)
    plt.plot(tf, 2.0/N * np.abs(zff[0:np.int(N/2)]), label="z")
    plt.grid()
    plt.legend()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Accelaration (g)')
    plt.title('Frequency Domain Vibration Analysis')

    plt.savefig(".\static\images\plot.png", format='png')
    plt.close()
    return render(request, 'frequency.html')
