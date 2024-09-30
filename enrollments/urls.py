from django.urls import path
from . import views
app_name= 'enrollments'
urlpatterns = [
    path('', views.enroll, name='enroll'),
    path('<int:id>', views.listing, name='listing'),
]