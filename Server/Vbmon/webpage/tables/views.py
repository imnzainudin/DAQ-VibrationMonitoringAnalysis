from django.shortcuts import render
import pandas as pd
import json
import os


def tables(request):
    path = '/Users'
    path = os.path.join(path, 'User/Desktop/ImanZainudin','Online_DAQ.csv')
    df = pd.read_csv(path)
    df = df.fillna("")
    json_records = df.reset_index().to_json(orient='records')
    array = []
    array = json.loads(json_records)
    contextt = {'d': array}
    return render(request, 'table.html', contextt)
