from django.shortcuts import render
from subprocess import run, PIPE
import sys

def button(request):
    return render(request, "index.html")

def output(request):
    print("Hello World from Python!")
    data = "THIS IS THE DATA"
    return render(request, "index.html", {'data':data})

def external(request):
    inp = request.POST.get('param')

    out = run([sys.executable, 'D:\\Dev\\CuseHacks2021\\client.py', inp], shell=False, stdout=PIPE)

    print(out)

    return render(request, 'index.html', {'data1': out.stdout})