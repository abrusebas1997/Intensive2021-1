from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Appointment

class AppointmentListView(ListView):
    """Shows users a list of appointments"""

    model = Appointment

class AppointmentDetailView(DetailView):
    """To show the user a single appointment"""
    model = Appointment


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new Appointment"""

    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment succesfully created'
