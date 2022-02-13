from django.shortcuts import render, redirect
from app.models import Tratamentos
from app.form import TratamentosForm


def home(request):
    data = {'db': Tratamentos.objects.all}
    return render(request, 'home.html', data)


def form(request):
    data = {'form': TratamentosForm()}
    return render(request, 'form.html', data)


def create(request):
    form = TratamentosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')