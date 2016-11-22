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
        match = isValidId(w_num);
        if not match: #if it does not match the pattern, give error
            message = "Invalid number, please enter your 8 digit W#"
            messages.success(request, message)
        else :
            w_num = match.group(1)
            message = processUserLogging(w_num)
            messages.success(request, message)
        # Redirect the web page to the same path but with the form now empty POST -> GET (avoid resubmission scenario)
            return HttpResponseRedirect(request.path)
    else:
        # Create a new form and pass it to the web page
        form = NameForm()
    return render(request, 'cardreader/index.html', {'form': form, 'w_num': w_num})

def isValidId(w_num):
    pattern = re.compile("W?([0-9]{8})")  # Possibly always add the W, or make sure it doesnt add any numbers after it, for using the card
    match = pattern.search(w_num)
    return match;

def processUserLogging(w_num):
    query = Student.objects.filter(w_num=w_num).filter(out_time=None).last()
    current_time = timezone.now()
    if query:
        dur = (current_time - query.in_time).seconds
        if (dur / 60 < 1):
            #User tried to swipe again within 60 seconds
            #Most likely accidental multiple swipe, ignore
            message = "You are already logged in " + w_num + " wait " + str(60-dur) + " seconds before logging out"
        else:
            in_time = query.in_time
            query.out_time = current_time
            dt = current_time - in_time
            query.duration = dt.seconds / 60
            query.save()
            # Compile message to be sent to web page
            message = "Thank you for logging out, " + w_num
    else:
        # Create a new instance of Student class and log student in
        student = Student(w_num=w_num, in_time=current_time)
        student.save()
        # Compile message to be sent to web page
        message = "Thank you for logging in, " + w_num

    return message