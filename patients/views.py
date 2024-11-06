from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserForm, PatientForm, AppointmentForm  # Correct form imports
from .models import Patient

# Registration view
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)  # Correct form reference
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        user_form = UserForm()
        patient_form = PatientForm()
    return render(request, 'patients/register.html', {'user_form': user_form, 'patient_form': patient_form})


# Patient dashboard view
def patient_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    return render(request, 'patients/dashboard.html', {'patient': patient})


import json
from django.shortcuts import render
from .models import Patient, Progress, Appointment

def patient_dashboard(request):
    # Get the patient object associated with the logged-in user
    patient = Patient.objects.get(user=request.user)
    
    # Query the progress and appointments for the patient
    progress = Progress.objects.filter(patient=patient).order_by('-date')
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')

    # Prepare data for JavaScript
    progress_data = {
        'dates': [p.date.strftime('%Y-%m-%d') for p in progress],
        'scores': [p.health_score for p in progress]
    }
    appointments_data = {
        'dates': [a.appointment_date.strftime('%Y-%m-%d') for a in appointments],  # Use appointment_date
        'counts': [1 for a in appointments]  # Example data: 1 for each appointment
    }

    # Prepare the context with the necessary data
    context = {
        'patient': patient,
        'progress_data': json.dumps(progress_data),
        'appointments_data': json.dumps(appointments_data),
    }

    return render(request, 'patients/dashboard.html', context)






# Appointment scheduling view
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.save()
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'patients/schedule_appointment.html', {'form': form})



from django.shortcuts import render

def home(request):
    return render(request, 'patients/home.html')


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient_dashboard')  # Redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'patients/login.html', {'form': form})



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page after logout


from django.shortcuts import redirect

def some_view(request):
    # Redirect to home view
    return redirect('home')  # Use the name defined in urls.py

from django.shortcuts import render

def dashboard(request):
    return render(request, 'patients/dashboard.html')  # Adjust the template path as needed


from django.shortcuts import render
from .models import GroupChat

def chat_view(request):
    group_chats = GroupChat.objects.all()  # Get all group chats
    return render(request, 'patients/chat.html', {'group_chats': group_chats})  # Pass it to the template


