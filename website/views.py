from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# need to import the forms.py 
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.

# created url first in url.py then created this function to communicate with urls.py
def home(request):
    # grabbing records to have them displayed
    records = Record.objects.all()

    # check to see if logging in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records' : records})

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out. ")
    return redirect('home')

def register_user(request):
    # now post the user reg
    if request.method == 'POST':
        form = SignUpForm(request.POST) # once filled out it will send it to the forms.py 
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] # grabbing first input 
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"You have successfully registered {username}")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form}) # step 2 -> now create a register.html file 
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You're not logged in, please login")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_user = Record.objects.get(id=pk)
        delete_user.delete()
        messages.success(request, f"Record has been deleted")
        return redirect('home')
    else:
        messages.success(request, "You're not logged in, please login")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Successfully created record.")
                return redirect('home')
        return render(request, 'add_record.html', {"form" : form}) 
    else:
        messages.success(request, "Must be logged in.")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record) # current record will proprogate what is already displayed
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated record.")
            return redirect('home')
        return render(request, 'update_record.html', {"form" : form})
    else:
        messages.success(request, "Must be logged in.")
        return redirect('home')

