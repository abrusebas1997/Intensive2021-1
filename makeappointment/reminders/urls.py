from django.conf.urls import re_path

from .views import (
    AppointmentCreateView,
    AppointmentListView,
    AppointmentDeleteView,
)

urlpatterns = [
    # Create, update, delete
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),
    re_path(r'^$', AppointmentListView.as_view(), name='list_appointments'),
    re_path(r'^/(?P[0-9]+)/delete$', AppointmentDeleteView.as_view(), name='delete_appointment'),

]
