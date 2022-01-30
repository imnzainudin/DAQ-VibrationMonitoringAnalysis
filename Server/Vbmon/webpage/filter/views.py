from django.shortcuts import render, redirect
import json
import pandas as pd
from scipy.fftpack import fft
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from .forms import DateForm


def custom(request):
    path = '/Users'
    path = os.path.join(path, 'User/Desktop/ImanZainudin', 'Online_DAQ.csv')
    df = pd.read_csv(path)
    df = df.fillna("")
    form = DateForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            data1 = form.cleaned_data["date1"]
            data2 = form.cleaned_data["date2"]
            #print(data1, data2)
            data1_time = pd.to_datetime(data1, format='%Y/%m/%d')
            data2_time = pd.to_datetime(data2, format='%Y/%m/%d')
            #print(data1_time, data2_time)
            after_start_date = pd.to_datetime(
                df["DateTime"], format='%Y/%m/%d') >= data1_time
            before_end_date = pd.to_datetime(
                df["DateTime"], format='%Y/%m/%d') <= data2_time
            between_two_dates = after_start_date & before_end_date
            #print(between_two_dates)
            filtered_dates = df.loc[between_two_dates]
            #print(filtered_dates)
            json_s = filtered_dates.reset_index().to_json(orient='records')
            array = []
            array = json.loads(json_s)
            #print(array)

            #If DataFrame Empty
            if filtered_dates.empty:
                return redirect('filter:empty')

            #Custom Time Domain Graph
            plt.plot(filtered_dates["TimeEpoch"],
                     filtered_dates["xaccelaration"], label="x")
            plt.plot(filtered_dates["TimeEpoch"],
                     filtered_dates["yaccelaration"], label="y")
            plt.plot(filtered_dates["TimeEpoch"],
                     filtered_dates["zaccelaration"], label="z")
            plt.legend()
            plt.xlabel("Time (s)", fontsize=12)
            plt.ylabel("Accelaration (g)", fontsize=12)
            plt.title("Time Domain Vibration Analysis", fontsize=12)
            plt.grid()

            plt.savefig(".\static\images\customgraph.png", format='png')
            plt.close()

            #Custom Frequency Domain Graph
            filtered_dates.reset_index(drop=True, inplace=True)
            t = filtered_dates["TimeEpoch"]
            x = filtered_dates["xaccelaration"]
            y = filtered_dates["yaccelaration"]
            z = filtered_dates["zaccelaration"]

            #------Variables
            N = np.int(np.prod(t.shape))
            N2 = 2**(N.bit_length()-1)
            Fs = 1/(t[1]-t[0])
            T = 1/Fs

            #print(filtered_dates)

            #------Compute FFT
            N = N2  # truncate array to the last power of 2
            tf = np.linspace(0.0, 1.0/(2.0*T), N//2)
            xff = fft(x.values, n=N)
            yff = fft(y.values, n=N)
            zff = fft(z.values, n=N)
            plt.plot(tf, 2.0/N * np.abs(xff[0:np.int(N/2)]), label="x")
            plt.plot(tf, 2.0/N * np.abs(yff[0:np.int(N/2)]), label="y")
            plt.plot(tf, 2.0/N * np.abs(zff[0:np.int(N/2)]), label="z")
            plt.grid()
            plt.legend()
            plt.xlabel('Frequency (Hz)')
            plt.ylabel('Accelaration (g)')
            plt.title('Frequency Domain Vibration Analysis')
            plt.savefig(".\static\images\customplot.png", format='png')
            plt.close()

        return render(request, 'custom.html', context={'form': form, 'array': array})

    else:
        form = DateForm()
        json_s = df.reset_index().to_json(orient='records')
        array = []
        array = json.loads(json_s)
        #print(array)

        #Time Domain Graph
        plt.plot(df["TimeEpoch"], df["xaccelaration"], label="x")
        plt.plot(df["TimeEpoch"], df["yaccelaration"], label="y")
        plt.plot(df["TimeEpoch"], df["zaccelaration"], label="z")
        plt.legend()
        plt.xlabel("Time (s)", fontsize=12)
        plt.ylabel("Accelaration (g)", fontsize=12)
        plt.title("Time Domain Vibration Analysis", fontsize=12)
        plt.grid()

        plt.savefig(".\static\images\customgraph.png", format='png')
        plt.close()

        #Frequency Domain Graph
        t = df["TimeEpoch"]
        x = df["xaccelaration"]
        y = df["yaccelaration"]
        z = df["zaccelaration"]

        #------Variables
        N = np.int(np.prod(t.shape))
        N2 = 2**(N.bit_length()-1)
        Fs = 1/(t[1]-t[0])
        T = 1/Fs

        #------Compute FFT
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
        plt.savefig(".\static\images\customplot.png", format='png')
        plt.close()

    return render(request, "custom.html", context={'form': form, 'array': array})


def empty(request):
    return render(request, "empty.html")

