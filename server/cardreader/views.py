import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib import messages

# Create your views here.

def index(request):
    name = "default"
    if request.method == 'POST':

        form = NameForm()

        name = request.POST['w_number']
        pattern = re.compile("(W[0-9]{8})")
        match = pattern.search(name)
        name = match.group(1)

        print('Just set name: ' + match.group(1))
        message = "Thank you, " + name
        messages.success(request, message)
        return HttpResponseRedirect(request.path)
    else:
        form = NameForm()
    return render(request, 'cardreader/index.html', {'form': form, 'name': name})

# def get_name(request):
#     name = "default"
#     if request.method == 'POST':
#         prev_form = NameForm(request.POST)
#         form = NameForm()
#
#         name = request.POST['w_number']
#         pattern = re.compile("(W[0-9]{8})")
#         match = pattern.search(name)
#         name = match.group(1)
#
#         print('Just set name: ' + match.group(1))
#
#     else:
#         form = NameForm()
#
#     return render(request, 'cardreader/name.html', {'form': form, 'name': name})
