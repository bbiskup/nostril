from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from nostril.tasks import dummy_output_ignore_state, mul

def simple_view(request):
    msg = str(datetime.now())
    dummy_output_ignore_state.delay(msg)
    return HttpResponse("ok")

def call_mul(request):
    r = mul.delay(1, 2).get()
    return HttpResponse("Result: " + str(r))
