import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import os


def time(request):
    path = '/Users'
    path = os.path.join(path, 'User/Desktop/ImanZainudin', 'Online_DAQ.csv')
    df = pd.read_csv(path)
    df = df.fillna("")
    plt.plot(df["TimeEpoch"], df["xaccelaration"], label="x")
    plt.plot(df["TimeEpoch"], df["yaccelaration"], label="y")
    plt.plot(df["TimeEpoch"], df["zaccelaration"], label="z")
    plt.legend()
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Accelaration (g)", fontsize=12)
    plt.title("Time Domain Vibration Analysis", fontsize=12)
    plt.grid()

    plt.savefig(".\static\images\graph.png", format='png')
    plt.close()
    return render(request, 'time.html')
