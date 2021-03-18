from django.conf.urls import re_path

from .views import (
    AppointmentCreateView,
)

urlpatterns = [
    # Create, update, delete
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),
    re_path(r'^$', AppointmentListView.as_view(), name='list_appointments'),
]
