import re, datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib import messages
from .models import Student
from django.utils import timezone


# Create your views here.

def index(request):
    w_num = "default"
    if request.method == 'POST':
        # Create a new form
        form = NameForm()

        # Use regex to parse out w_number
        w_num = request.POST['w_number']
        pattern = re.compile("W?([0-9]{8})")  # Possibly always add the W, or make sure it doesnt add any numbers after it, for using the card
        match = pattern.search(w_num)

        if not match: #if it does not match the pattern, give error
            message = "Invalid number, please enter your 8 digit W#"
            messages.success(request, message)
        # w_num = match.group(1)
        else :
            w_num = match.group(1)
            query = Student.objects.filter(w_num=w_num).filter(out_time=None).last()
            if query:  # log user out
                current_time = timezone.now()
                in_time = query.in_time
            	query.out_time = current_time
                dt = current_time - in_time
                duration = dt.seconds
                query.total_time = duration / 60
                query.save()
                # Compile message to be sent to web page
                message = "Thank you for logging out, " + w_num
                messages.success(request, message)
            else:
                # Create a new instance of Student class and log student in
                current_time = timezone.now()
                student = Student(w_num=w_num, in_time=current_time)
                student.save()
                # Compile message to be sent to web page
                message = "Thank you for logging in, " + w_num
                messages.success(request, message)

        # Redirect the web page to the same path but with the form now empty POST -> GET (avoid resubmission scenario)
            return HttpResponseRedirect(request.path)
    else:
        # Create a new form and pass it to the web page
        form = NameForm()
    return render(request, 'cardreader/index.html', {'form': form, 'w_num': w_num})
