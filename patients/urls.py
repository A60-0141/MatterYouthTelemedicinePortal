
from django.urls import path
from . import views
from .views import home
from .views import chat_view

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ensure login URL is defined here
    # path('logout/', views.logout_view, name='logout'),  # Comment out this line
    path('register/', views.register, name='register'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('schedule/', views.schedule_appointment, name='schedule_appointment'),
    path('', home, name='home'),
    path('chat/', chat_view, name='chat'), 
]