import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib import messages

# Create your views here.

def index(request):
    name = "default"
    if request.method == 'POST':
        # Create a new form
        form = NameForm()

        # Use regex to parse out w_number
        name = request.POST['w_number']
        pattern = re.compile("(W[0-9]{8})")  # Could take 'W' out of parenthesis to only capture 8 digits
        match = pattern.search(name)
        name = match.group(1)

        # Compile message to be sent to web page
        message = "Thank you, " + name
        messages.success(request, message)

        # Redirect the web page to the same path but with the form now empty POST -> GET (avoid resubmission scenario)
        return HttpResponseRedirect(request.path)
    else:
        # Create a new form and pass it to the web page
        form = NameForm()
    return render(request, 'cardreader/index.html', {'form': form, 'name': name})
