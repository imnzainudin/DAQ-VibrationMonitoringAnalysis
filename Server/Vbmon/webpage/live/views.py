from django.shortcuts import render
import pandas as pd
import os
import json


def live(request):
    return render(request, "live.html")
