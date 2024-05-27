from django.shortcuts import render, redirect
from .forms import ApplicationForm

def application_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'applications/application_form.html', {'form': form})

def success(request):
    return render(request, 'applications/success.html')
