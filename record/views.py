from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, RecordForm
from .models import Record


#home page  
def home(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        
        return render(request,'home.html',{'records':records})
    else:
        #check for login status
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Logged in!")
                return redirect('home')
            else:
                messages.success(request, "Invalid details!!")
                return redirect('home')
        else:
            return render(request, 'home.html',{'records':records})
    
        
    

#logout page    
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out!")
    return redirect('home')


#registration page  
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registered")
            return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    

    
#reord page 
def patient_record(request, pk):
    if request.user.is_authenticated:
        patient_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'patient_record':patient_record})
    else:
        messages.success(request, "You must login first!")
        return redirect('home')
    

    
#delete record  
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted...")
        return redirect('home')
    else:
        messages.success(request, "You must login first...")
        return redirect('home')
    

#add record page    
def add_record(request):
    if request.POST:
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, "Record added....")
            return redirect('home')
        else:
            form = RecordForm()
            return render(request, 'add_record.html', {'form':form}) 
    else:
        form = RecordForm()
        return render(request, 'add_record.html', {'form':form})
    
    

def edit_record(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)
        
        if request.method == 'POST':
            form = RecordForm(request.POST, instance=record)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Record edited...")
                return redirect('home')
        else:
            form = RecordForm(instance=record)
        
        return render(request, 'edit.html', {'form': form, 'record':record})
    

